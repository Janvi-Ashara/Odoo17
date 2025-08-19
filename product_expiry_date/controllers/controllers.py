# -*- coding: utf-8 -*-
# from odoo import http


# class ProductExpiryDate(http.Controller):
#     @http.route('/product_expiry_date/product_expiry_date', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_expiry_date/product_expiry_date/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_expiry_date.listing', {
#             'root': '/product_expiry_date/product_expiry_date',
#             'objects': http.request.env['product_expiry_date.product_expiry_date'].search([]),
#         })

#     @http.route('/product_expiry_date/product_expiry_date/objects/<model("product_expiry_date.product_expiry_date"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_expiry_date.object', {
#             'object': obj
#         })

