from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_reference = fields.Char(string="Project Reference")

    @api.onchange('partner_id')
    def _onchange_partner_id1(self):
        self.write({
            'project_reference': self.partner_id.project_reference
        })
