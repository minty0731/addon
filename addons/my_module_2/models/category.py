from odoo import api, fields, models

class Category(models.Model):
    _name = 'my.module.category'
    _description = 'Category Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    product_ids = fields.One2many('my.module.product', 'category_id', string='Products')
