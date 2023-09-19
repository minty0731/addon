from odoo import api, fields, models, _

class Product(models.Model):
    _name = 'my.module.product'
    _description = 'Product Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('my.module.category', string='Category')

    _sql_constraints = [
        ('name_uniq_within_category', 'unique(name, category_id)', 'Product name need to be unique!')
    ]
