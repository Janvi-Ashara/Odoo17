from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer_name = fields.Char(string='Manufacturer Name', help='Name of the product manufacturer')