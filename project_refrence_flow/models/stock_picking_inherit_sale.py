from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _prepare_stock_picking_vals(self, order):
        vals = super()._prepare_stock_picking_vals(order)
        vals['project_reference'] = order.project_reference
        return vals
