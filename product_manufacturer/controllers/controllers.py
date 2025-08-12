# -*- coding: utf-8 -*-
# from odoo import http


# class ProductManufacturer(http.Controller):
#     @http.route('/product_manufacturer/product_manufacturer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_manufacturer/product_manufacturer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_manufacturer.listing', {
#             'root': '/product_manufacturer/product_manufacturer',
#             'objects': http.request.env['product_manufacturer.product_manufacturer'].search([]),
#         })

#     @http.route('/product_manufacturer/product_manufacturer/objects/<model("product_manufacturer.product_manufacturer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_manufacturer.object', {
#             'object': obj
#         })

