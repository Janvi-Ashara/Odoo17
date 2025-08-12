from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    project_reference = fields.Char(string="Project Reference")
