import datetime

from odoo import fields, models, api


class KnowledgePosts(models.Model):
    _name = 'knowledge.posts'
    _description = 'Knowledge Post'

    name = fields.Char(string='Tiêu đề bài viết')
    date_of_writing = fields.Datetime(default=datetime.datetime.now(), string='Chỉnh sửa lần cuối')
    content = fields.Html(string='Nội dung')
    tac_gia = fields.Many2one('res.users', string='Tác giả', default=lambda lm: lm.env.user, readonly=True)
    # check_admin_tac_gia = fields.Boolean(compute='_check_admin')
    group = fields.Many2one('access.right')

    # @api.depends('tac_gia')
    # def _check_admin(self):
    #     for rec in self:
    #         # print('caculate===========')
    #         if 2 in rec.tac_gia.groups_id.ids:
    #             rec.check_admin_tac_gia = True
    #         else:
    #             rec.check_admin_tac_gia = False
    #         # print(rec.check_admin_tac_gia)

    # @api.onchange('name')
    # def _check_asd(self):
    #     # for rec in self:
    #     print('asfasf================')
    #     print(self.group)
    #     print((self.content))