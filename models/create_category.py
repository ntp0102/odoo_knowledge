# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateCategory(models.Model):
    _name = 'create.category'
    _description = 'create category'

    category = fields.Char(string='Category',required=True)