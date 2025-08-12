from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_note = fields.Text(string='Discount Note', help='Additional information about discounts applied')