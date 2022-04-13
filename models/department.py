# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'department'
    _description = 'Department Name'

    name = fields.Char('Tên phòng ban', required=True)
    field_list = fields.Char('Tên bộ phận')
