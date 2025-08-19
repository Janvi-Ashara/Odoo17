# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_expiry_date(models.Model):
#     _name = 'product_expiry_date.product_expiry_date'
#     _description = 'product_expiry_date.product_expiry_date'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

