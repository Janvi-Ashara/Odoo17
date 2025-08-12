from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    project_reference = fields.Char(string="Project Reference")
