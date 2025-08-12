# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectRefrenceFlow(http.Controller):
#     @http.route('/project_refrence_flow/project_refrence_flow', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_refrence_flow/project_refrence_flow/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_refrence_flow.listing', {
#             'root': '/project_refrence_flow/project_refrence_flow',
#             'objects': http.request.env['project_refrence_flow.project_refrence_flow'].search([]),
#         })

#     @http.route('/project_refrence_flow/project_refrence_flow/objects/<model("project_refrence_flow.project_refrence_flow"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_refrence_flow.object', {
#             'object': obj
#         })

