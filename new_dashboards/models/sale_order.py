from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_sale_order_amount = fields.Float(string="Total Sale Order", compute="_compute_total_sale_order_amount", store=False)

    @api.depends("order_line.price_total", "state")
    def _compute_total_sale_order_amount(self):
        for order in self:
            if order.state in ["sale", "done"]:
                order.total_sale_order_amount = sum(order.order_line.mapped("price_total"))
            else:
                order.total_sale_order_amount = 0.0

    @api.model
    def get_sales_tiles_data(self):
        """Return sales dashboard summary"""
        quotations = self.env["sale.order"].search_count([("state", "in", ["draft", "sent"])])
        orders = self.env["sale.order"].search_count([("state", "=", "sale")])
        invoices = self.env["account.move"].search_count([("move_type", "=", "out_invoice")])
        amount = sum(self.env["sale.order"].search([]).mapped("amount_total"))
        total_sale_order_amount = sum(
            self.env["sale.order"].search([("state", "in", ["sale", "done"])]).mapped("total_sale_order_amount"))
        total_sale_order = self.env["sale.order"].search_count([]) #only show total sale orders

        return {
            "quotations": quotations,
            "orders": orders,
            "invoices": invoices,
            "amount": amount,
            "total_sale_order_amount": total_sale_order_amount,
            "total_sale_order" : total_sale_order
        }
