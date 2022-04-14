import datetime

from odoo import fields, models, api


class KnowledgePosts(models.Model):
    _name = 'knowledge.posts'
    _description = 'Description'

    title = fields.Char(string='Tiêu đề bài viết')
    date_of_writing = fields.Datetime(compute='_onchange_date_of_writing', string='Chỉnh sửa lần cuối')
    content = fields.Html(string='Nội dung')
    tac_gia = fields.Many2one('res.users', string='Tác giả', default=lambda lm: lm.env.user)

    @api.depends('content')
    def _onchange_date_of_writing(self):
        self.date_of_writing = datetime.datetime.now()