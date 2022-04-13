# -*- coding: utf-8 -*-
# from odoo import http


# class Knowledge(http.Controller):
#     @http.route('/knowledge/knowledge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/knowledge/knowledge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('knowledge.listing', {
#             'root': '/knowledge/knowledge',
#             'objects': http.request.env['knowledge.knowledge'].search([]),
#         })

#     @http.route('/knowledge/knowledge/objects/<model("knowledge.knowledge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('knowledge.object', {
#             'object': obj
#         })
