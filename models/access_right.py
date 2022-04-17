# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccessRight(models.Model):
    _name = 'access.right'
    _description = 'Phân quyền cho các bài viết'

    knowledge_posts = fields.Many2one('knowledge.posts', required=True)
    res_group = fields.Many2one('res.groups')
