# -*- coding: utf-8 -*-
# from odoo import http


# class MiniSalePurchaseDashboard(http.Controller):
#     @http.route('/mini_sale_purchase_dashboard/mini_sale_purchase_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mini_sale_purchase_dashboard/mini_sale_purchase_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mini_sale_purchase_dashboard.listing', {
#             'root': '/mini_sale_purchase_dashboard/mini_sale_purchase_dashboard',
#             'objects': http.request.env['mini_sale_purchase_dashboard.mini_sale_purchase_dashboard'].search([]),
#         })

#     @http.route('/mini_sale_purchase_dashboard/mini_sale_purchase_dashboard/objects/<model("mini_sale_purchase_dashboard.mini_sale_purchase_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mini_sale_purchase_dashboard.object', {
#             'object': obj
#         })

