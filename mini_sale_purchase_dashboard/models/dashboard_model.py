from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class DashboardSalesPurchase(models.Model):
    _name = 'mini_sale_purchase_dashboard.sales_purchase'
    _description = 'Sales and Purchase Dashboard'

    name = fields.Char(string="Dashboard Name", default="Sales & Purchase Dashboard")

    total_sales_this_month = fields.Integer(
        string="Sales Orders",
        compute='_compute_sales_orders',
        store=True
    )
    total_purchase_this_month = fields.Integer(
        string="Purchase Orders",
        compute='_compute_purchase_orders',
        store=True
    )
    total_invoices_this_month = fields.Integer(
        string="Invoices",
        compute='_compute_invoices',
        store=True
    )


    @api.depends()
    def _compute_sales_orders(self):
        """Compute total sales orders for the current month."""
        for record in self:
            today_local = fields.Date.context_today(self)
            first_day_of_month = today_local.replace(day=1)
            last_day_of_month = fields.Date.end_of(today_local, 'month')

            record.total_sales_this_month = self.env['sale.order'].search_count([
                ('date_order', '>=', first_day_of_month),
                ('date_order', '<=', last_day_of_month),
                ('state', 'in', ['sale', 'done']),
            ])
            _logger.info(f"Sales Orders (this month): {record.total_sales_this_month}")


    @api.depends()
    def _compute_purchase_orders(self):
        """Compute total purchase orders for the current month."""
        for record in self:
            today_local = fields.Date.context_today(self)
            first_day_of_month = today_local.replace(day=1)
            last_day_of_month = fields.Date.end_of(today_local, 'month')

            record.total_purchase_this_month = self.env['purchase.order'].search_count([
                ('date_order', '>=', first_day_of_month),
                ('date_order', '<=', last_day_of_month),
                ('state', 'in', ['purchase', 'done']),
            ])
            _logger.info(f"Purchase Orders (this month): {record.total_purchase_this_month}")


    @api.depends()
    def _compute_invoices(self):
        """Compute total customer invoices for the current month."""
        for record in self:
            today_local = fields.Date.context_today(self)
            first_day_of_month = today_local.replace(day=1)
            last_day_of_month = fields.Date.end_of(today_local, 'month')

            record.total_invoices_this_month = self.env['account.move'].search_count([
                ('invoice_date', '>=', first_day_of_month),
                ('invoice_date', '<=', last_day_of_month),
                ('state', '=', 'posted'),
                ('move_type', '=', 'out_invoice'),
            ])
            _logger.info(f"Invoices (this month): {record.total_invoices_this_month}")


    def refresh_dashboard(self):
        """Force refresh of dashboard data"""
        self._compute_sales_orders()
        self._compute_purchase_orders()
        self._compute_invoices()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    @api.model
    def create_default_dashboard(self):
        """Create default dashboard if none exists"""
        existing = self.search([], limit=1)
        if not existing:
            dashboard = self.create({'name': 'Sales & Purchase Dashboard'})
            # Trigger computations
            dashboard._compute_sales_orders()
            dashboard._compute_purchase_orders()
            dashboard._compute_invoices()
            return dashboard
        return existing