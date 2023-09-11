from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"

    color = fields.Integer(string='Color')
    name = fields.Char(string="Name", required=True)
    _sql_constraints = [
        ('tag_name_unique', 'UNIQUE(name)', 'The tag name must be unique!'),
    ]
