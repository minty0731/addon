from odoo import models, fields, api

class Category(models.Model):
    _name = 'my_module.category'
    _description = 'Product Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    product_ids = fields.One2many('my_module.product', 'category_id', string='Products')

class Product(models.Model):
    _name = 'my_module.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('my_module.category', string='Category')

    _sql_constraints = [
        ('name_category_uniq', 'unique(name, category_id)', 'Product Name must be unique within a Category!'),
    ]
