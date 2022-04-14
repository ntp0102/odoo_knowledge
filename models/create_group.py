# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateGroup(models.Model):
    _inherit = 'res.groups'
    _description = 'add user to group'

