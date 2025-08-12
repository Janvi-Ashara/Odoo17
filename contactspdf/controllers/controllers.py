# -*- coding: utf-8 -*-
# from odoo import http


# class Contactspdf(http.Controller):
#     @http.route('/contactspdf/contactspdf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contactspdf/contactspdf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contactspdf.listing', {
#             'root': '/contactspdf/contactspdf',
#             'objects': http.request.env['contactspdf.contactspdf'].search([]),
#         })

#     @http.route('/contactspdf/contactspdf/objects/<model("contactspdf.contactspdf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contactspdf.object', {
#             'object': obj
#         })

