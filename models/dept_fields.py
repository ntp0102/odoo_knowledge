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
        vals = {
            'field_list': self.dependent
        }
        self.env['department'].browse(self.dependent.ids).write(vals)
        print('self.dependent: + ', self.browse(self.name))
        print('type----', type(self.browse(self.name)))
        return super(Dept_Fields, self).create(values)
