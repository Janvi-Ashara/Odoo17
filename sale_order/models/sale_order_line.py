from odoo import fields, models
from odoo.api import ondelete

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_id = fields.Many2one(
        'product.product',
        domain=[('sale_ok', '=', True)],
        string="Product",
        ondelete='restrict',
        required=True,
    )
