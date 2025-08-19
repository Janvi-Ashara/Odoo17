from odoo import fields, models, api
from datetime import date


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_rating = fields.Selection(
        selection=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], string='Customer Rating',
        default='0')

