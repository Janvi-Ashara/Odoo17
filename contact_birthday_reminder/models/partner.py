from odoo import api, fields, models
from datetime import date


class ResPartner(models.Model):
    _inherit = "res.partner"

    date_of_birth = fields.Date(string="Date of Birth")
    age_years = fields.Integer(string="Age", compute="_compute_age_years", store=True, )
    is_birthday_today = fields.Boolean(string="Birthday Today", compute="_compute_is_birthday_today", store=True, )

    @api.depends("date_of_birth")
    def _compute_age_years(self):
        today = date.today()
        for partner in self:
            if partner.date_of_birth:
                partner.age_years = today.year - partner.date_of_birth.year - (
                        (today.month, today.day) < (partner.date_of_birth.month, partner.date_of_birth.day)
                )
            else:
                partner.age_years = 0

    @api.depends("date_of_birth")
    def _compute_is_birthday_today(self):
        today = date.today()
        for partner in self:
            dob = partner.date_of_birth
            partner.is_birthday_today = bool(
                dob and dob.month == today.month and dob.day == today.day
            )
