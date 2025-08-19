# -*- coding: utf-8 -*-
# from odoo import http


# class SimpleStockReport(http.Controller):
#     @http.route('/simple_stock_report/simple_stock_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple_stock_report/simple_stock_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple_stock_report.listing', {
#             'root': '/simple_stock_report/simple_stock_report',
#             'objects': http.request.env['simple_stock_report.simple_stock_report'].search([]),
#         })

#     @http.route('/simple_stock_report/simple_stock_report/objects/<model("simple_stock_report.simple_stock_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple_stock_report.object', {
#             'object': obj
#         })

