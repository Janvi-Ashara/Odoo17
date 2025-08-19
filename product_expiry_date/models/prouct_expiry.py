from odoo import models, fields, api
from datetime import date, timedelta


class ProductTemplate(models.Model):
    _inherit = "product.template"

    expiry_date = fields.Date("Expiry Date", help="Enter Product Expiry Date")
    expiry_warning = fields.Boolean(compute="_compute_expiry_status", store=False)
    expiry_message = fields.Char(compute="_compute_expiry_status", store=False)

    @api.depends("expiry_date")
    def _compute_expiry_status(self):
        for rec in self:
            if rec.expiry_date:
                days_left = (rec.expiry_date - date.today()).days
                if 0 <= days_left <= 30:
                    rec.expiry_warning = True
                    rec.expiry_message = "This product will expire within 30 days!"
                elif days_left < 0:
                    rec.expiry_warning = True
                    rec.expiry_message = "This product has already expired!"
                else:
                    rec.expiry_warning = False
                    rec.expiry_message = False
            else:
                rec.expiry_warning = False
                rec.expiry_message = False
