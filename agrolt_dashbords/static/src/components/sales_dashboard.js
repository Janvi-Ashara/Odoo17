/** @odoo-module **/

import { registry } from "@web/core/registry";
import { KpiCard } from "./kpi_card/kpi_card";
import { ChartRenderer } from "./chart_render/chart_renderer";
import { useService } from "@web/core/utils/hooks";

const { Component, onWillStart, useState } = owl;

export class OwlSalesDashboard extends Component {
  setup() {
    this.orm = useService("orm");
    this.actionService = useService("action");

    this.state = useState({
      quotations: { value: 0, percentage: 0 },
      orders: { value: 0, percentage: 0 },
      revenue: { value: 0, percentage: 0 },
      avg_order: { value: 0, percentage: 0 },
      period: 0,
      current_date: false,
      previous_date: false,
      topProducts: { labels: [], values: [], percentages: [] },
      topSalespersons: { labels: [], values: [], percentages: [] },
      monthlySales: { labels: [], values: [] },
      topSaleOrders: { labels: [], values: [] },
    });

    onWillStart(async () => {
      // Default load for KPIs + Top Products + Top Salespersons (with 7 days filter)
      await this.onPeriodChange({ target: { value: "7" } });

      // Load other graphs only once (no date filtering)
      await this._getMonthlySales();
      await this._getTopSaleOrders();
    });
  }

  // Handle Period Change (refresh KPI Cards + Top Products + Top Salespersons)
  async onPeriodChange(ev) {
    const days = parseInt(ev.target.value) || 0;
    this.state.period = days;

    if (days > 0) {
      const today = new Date();

      // Current period start
      const pastDate = new Date();
      pastDate.setDate(today.getDate() - days);
      this.state.current_date = pastDate.toISOString().slice(0, 19).replace("T", " ");

      // Previous period start
      const prevDate = new Date();
      prevDate.setDate(today.getDate() - days * 2);
      this.state.previous_date = prevDate.toISOString().slice(0, 19).replace("T", " ");
    } else {
      this.state.current_date = false;
      this.state.previous_date = false;
    }

    // Reload KPI Cards, Top Products, and Top Salespersons
    await Promise.all([
      this.getQuotations(),
      this.getOrders(),
      this.getRevenueAndAverage(),
      this.getTopProducts(),
      this.getTopSalespersons(),
    ]);
  }

  // Quotations (draft/sent)
  async getQuotations() {
    let domain = [["state", "in", ["draft", "sent"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    const count = await this.orm.searchCount("sale.order", domain);
    this.state.quotations.value = count;

    // Previous period data
    let prev_domain = [["state", "in", ["draft", "sent"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.previous_date],
        ["date_order", "<=", this.state.current_date]
      );
    }

    const prev_data = await this.orm.searchCount("sale.order", prev_domain);

    this.state.quotations.percentage = this._calculatePercentage(count, prev_data);
  }

  // Orders (confirmed/done)
  async getOrders() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }
    const count = await this.orm.searchCount("sale.order", domain);
    this.state.orders.value = count;

    let prev_domain = [["state", "in", ["sale", "done"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.previous_date],
        ["date_order", "<=", this.state.current_date]
      );
    }

    const prev_data = await this.orm.searchCount("sale.order", prev_domain);
    this.state.orders.percentage = this._calculatePercentage(count, prev_data);
  }

  // Revenue + Average Order
  async getRevenueAndAverage() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    const result = await this.orm.readGroup(
      "sale.order",
      domain,
      ["amount_total:sum"],
      []
    );

    let totalRevenue = result.length > 0 ? result[0].amount_total || 0 : 0;
    let totalOrders = result.length > 0 ? result[0].__count || 0 : 0;

    // Previous period
    let prev_domain = [["state", "in", ["sale", "done"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.previous_date],
        ["date_order", "<=", this.state.current_date]
      );
    }

    const prev_result = await this.orm.readGroup(
      "sale.order",
      prev_domain,
      ["amount_total:sum"],
      []
    );

    let prevRevenue = prev_result.length > 0 ? prev_result[0].amount_total || 0 : 0;
    let prevOrders = prev_result.length > 0 ? prev_result[0].__count || 0 : 0;

    // Revenue
    this.state.revenue.value = totalRevenue.toFixed(2);
    this.state.revenue.percentage = this._calculatePercentage(totalRevenue, prevRevenue);

    // Average order
    const avgOrderValue = totalOrders > 0 ? totalRevenue / totalOrders : 0;
    const prevAvgOrderValue = prevOrders > 0 ? prevRevenue / prevOrders : 0;
    this.state.avg_order = {
      value: avgOrderValue.toFixed(2),
      percentage: this._calculatePercentage(avgOrderValue, prevAvgOrderValue),
    };
  }

  // Top Products

async getTopProducts() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
        domain.push(["order_id.date_order", ">", this.state.current_date]);
    }

    const result = await this.orm.readGroup(
        "sale.order.line",
        domain,
        ["product_id", "product_uom_qty:sum"],
        ["product_id"],
        { limit: 5, orderby: "product_uom_qty:sum desc" }
    );

    // Previous period
    let prev_domain = [["state", "in", ["sale", "done"]]];
    if (this.state.period > 0) {
        prev_domain.push(
            ["order_id.date_order", ">", this.state.previous_date],
            ["order_id.date_order", "<=", this.state.current_date]
        );
    }

    const prev_result = await this.orm.readGroup(
        "sale.order.line",
        prev_domain,
        ["product_id", "product_uom_qty:sum"],
        ["product_id"],
        { limit: 5, orderby: "product_uom_qty:sum desc" }
    );

    const labels = result.map(r => r.product_id?.[1] || "Unknown");
    const values = result.map(r => r.product_uom_qty);

    // Previous values map
    const prevMap = {};
    prev_result.forEach(r => {
        prevMap[r.product_id?.[0]] = r.product_uom_qty;
    });

    // Percentage change vs previous period
    const percentages = result.map(r => {
        const prevVal = prevMap[r.product_id?.[0]] || 0;
        return this._calculatePercentage(r.product_uom_qty, prevVal);
    });

    // Replace state object (reactivity-safe)
    this.state.topProducts = {
        labels: [...labels],
        values: [...values],
        percentages: [...percentages],
    };
}

  // Top Salespersons
  async getTopSalespersons() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    const result = await this.orm.readGroup(
      "sale.order",
      domain,
      ["user_id", "amount_total:sum"],
      ["user_id"],
      { limit: 5, orderby: "amount_total:sum desc" }
    );

    // Previous period
    let prev_domain = [["state", "in", ["sale", "done"]]];
    if (this.state.period > 0) {
      prev_domain.push(
        ["date_order", ">", this.state.previous_date],
        ["date_order", "<=", this.state.current_date]
      );
    }

    const prev_result = await this.orm.readGroup(
      "sale.order",
      prev_domain,
      ["user_id", "amount_total:sum"],
      ["user_id"],
      { limit: 5, orderby: "amount_total:sum desc" }
    );

    const prevMap = {};
    prev_result.forEach(r => {
      prevMap[r.user_id?.[0]] = r.amount_total;
    });

    const labels = result.map(r => r.user_id ? r.user_id[1] : "Anonymous");
    const values = result.map(r => r.amount_total);
    const percentages = result.map(r => {
      const prevVal = prevMap[r.user_id?.[0]] || 0;
      return this._calculatePercentage(r.amount_total, prevVal);
    });

    // Replace full object (reactivity safe)
    this.state.topSalespersons = {
      labels: [...labels],
      values: [...values],
      percentages: [...percentages],
    };
  }

  // Monthly Sales (full data, no filter)
  async _getMonthlySales() {
    let domain = [["state", "in", ["sale", "done"]]];

    const result = await this.orm.readGroup(
      "sale.order",
      domain,
      ["amount_total:sum"],
      ["date_order:month"],
      { orderby: "date_order:month" }
    );

    this.state.monthlySales = {
      labels: result.map(r => r["date_order:month"]),
      values: result.map(r => r.amount_total),
    };
  }

  // Top Sale Orders (full data, no filter)
  async _getTopSaleOrders() {
    let domain = [["state", "in", ["sale", "done"]]];

    const result = await this.orm.readGroup(
      "sale.order",
      domain,
      ["amount_total:sum", "partner_id"],
      ["partner_id"],
      { limit: 5, orderby: "amount_total:sum desc" }
    );

    const partnerIds = result
      .map(r => Array.isArray(r.partner_id) ? r.partner_id[0] : r.partner_id)
      .filter(id => id);

    const partners = await this.orm.read("res.partner", partnerIds, ["name"]);
    const partnerMap = Object.fromEntries(partners.map(p => [p.id, p.name]));

    this.state.topSaleOrders = {
      labels: result.map(r => {
        let customerName = "Anonymous";
        const partnerId = Array.isArray(r.partner_id) ? r.partner_id[0] : r.partner_id;
        if (partnerId && partnerMap[partnerId]) {
          customerName = partnerMap[partnerId];
        }
        return customerName;
      }),
      values: result.map(r => r.amount_total),
    };
  }

  // Utility
  _calculatePercentage(current, prev) {
    if (prev > 0) {
      return (((current - prev) / prev) * 100).toFixed(2);
    } else if (current > 0) {
      return "100.00";
    }
    return "0.00";
  }

  // Actions
  viewQuotation() {
    this.actionService.doAction("sale.action_quotations_with_onboarding", {
      additionalContext: {
        search_default_draft: 1,
        search_default_my_quotation: 2,
      },
    });
  }

  viewOrders() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    this.actionService.doAction({
      type: "ir.actions.act_window",
      name: "Orders",
      res_model: "sale.order",
      domain,
      context: { group_by: ["date_order"] },
      views: [
        [false, "list"],
        [false, "form"],
      ],
    });
  }

  viewRevenues() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    this.actionService.doAction({
      type: "ir.actions.act_window",
      name: "Revenue",
      res_model: "sale.order",
      domain,
      context: { group_by: ["date_order"] },
      views: [
        [false, "pivot"],
        [false, "form"],
      ],
    });
  }

  viewAvgOrders() {
    let domain = [["state", "in", ["sale", "done"]]];
    if (this.state.current_date) {
      domain.push(["date_order", ">", this.state.current_date]);
    }

    this.actionService.doAction({
      type: "ir.actions.act_window",
      name: "Average Order Value",
      res_model: "sale.order",
      domain,
      context: { group_by: ["user_id"] },
      views: [
        [false, "pivot"],
        [false, "list"],
        [false, "form"],
      ],
    });
  }
}

OwlSalesDashboard.template = "owl.OwlSalesDashboard";
OwlSalesDashboard.components = { KpiCard, ChartRenderer };
registry.category("actions").add("owl.sales_dashboard", OwlSalesDashboard);
