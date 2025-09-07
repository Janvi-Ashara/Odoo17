# -*- coding: utf-8 -*-
# from odoo import http


# class AgroltDashbords(http.Controller):
#     @http.route('/agrolt_dashbords/agrolt_dashbords', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agrolt_dashbords/agrolt_dashbords/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agrolt_dashbords.listing', {
#             'root': '/agrolt_dashbords/agrolt_dashbords',
#             'objects': http.request.env['agrolt_dashbords.agrolt_dashbords'].search([]),
#         })

#     @http.route('/agrolt_dashbords/agrolt_dashbords/objects/<model("agrolt_dashbords.agrolt_dashbords"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agrolt_dashbords.object', {
#             'object': obj
#         })

