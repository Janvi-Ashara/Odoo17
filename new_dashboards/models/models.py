# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class new_dashboards(models.Model):
#     _name = 'new_dashboards.new_dashboards'
#     _description = 'new_dashboards.new_dashboards'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

