from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my_module.mymodel'
    _description = 'My Custom Model'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')
    active = fields.Boolean(string='Active', default=True)

    def set_amount(self):
        self.amount = 100.0 

        