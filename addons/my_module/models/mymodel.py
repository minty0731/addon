from odoo import api, fields, models

class MyModel(models.Model):
    _name = 'my.module.mymodel'
    _description = 'My Custom Model'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')
    active = fields.Boolean(string='Active', default=True)
