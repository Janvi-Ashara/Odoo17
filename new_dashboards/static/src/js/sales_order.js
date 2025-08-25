/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart, useState } from "@odoo/owl";

class SalesDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            quotations: 0,
            orders: 0,
            invoices: 0,
            amount: 0,
            total_sale_order_amount : 0,
            total_sale_order : 0,
        });

        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        const result = await this.orm.call("sale.order", "get_sales_tiles_data", []);
        this.state.quotations = result.quotations;
        this.state.orders = result.orders;
        this.state.invoices = result.invoices;
        this.state.amount = result.amount;
        this.state.total_sale_order_amount = result.total_sale_order_amount;
        this.state.total_sale_order = result.total_sale_order;
    }
}

SalesDashboard.template = "new_dashboards.SalesDashboard";

registry.category("actions").add("sales_dashboard_tag", SalesDashboard);
