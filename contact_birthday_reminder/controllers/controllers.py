# -*- coding: utf-8 -*-
# from odoo import http


# class ContactBirthdayReminder(http.Controller):
#     @http.route('/contact_birthday_reminder/contact_birthday_reminder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_birthday_reminder/contact_birthday_reminder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_birthday_reminder.listing', {
#             'root': '/contact_birthday_reminder/contact_birthday_reminder',
#             'objects': http.request.env['contact_birthday_reminder.contact_birthday_reminder'].search([]),
#         })

#     @http.route('/contact_birthday_reminder/contact_birthday_reminder/objects/<model("contact_birthday_reminder.contact_birthday_reminder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_birthday_reminder.object', {
#             'object': obj
#         })

