from odoo import api, fields, models

class MyModel(models.Model):
    _name = 'my.module.mymodel'
    _description = 'My Custom Model'


    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
    genre = fields.Char(string='Genre')

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')
    active = fields.Boolean(string='Active', default=True)

    def custom_action_method(self):
        self.write({'title': 'Updated Title'})
        return True
