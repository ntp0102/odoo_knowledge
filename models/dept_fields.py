# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dept_Fields(models.Model):
    _name = 'dept.fields'
    _description = 'Dept Fields'

    name = fields.Char(string='Tên bộ phận', required=True)
    dependent = fields.Many2one('department',string='Thuộc phòng ban')

    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""

        return super(Dept_Fields, self).create(values)
