# -*- coding: utf-8 -*-
# from odoo import http


# class NewDashboards(http.Controller):
#     @http.route('/new_dashboards/new_dashboards', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_dashboards/new_dashboards/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_dashboards.listing', {
#             'root': '/new_dashboards/new_dashboards',
#             'objects': http.request.env['new_dashboards.new_dashboards'].search([]),
#         })

#     @http.route('/new_dashboards/new_dashboards/objects/<model("new_dashboards.new_dashboards"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_dashboards.object', {
#             'object': obj
#         })

