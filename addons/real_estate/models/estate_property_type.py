from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "sequence, name"

    offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string='Offers')
    sequence = fields.Integer(string='Sequence')

    name = fields.Char(string="Type", required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    offer_count = fields.Integer(string='Offer Count', compute='_compute_offer_count')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def action_show_offers(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Offers',
            'res_model': 'estate.property.offer',
            'view_mode': 'tree,form',
            'domain': [('property_type_id', '=', self.id)],
        }

    _sql_constraints = [
        ('type_name_unique', 'UNIQUE(name)', 'The type name must be unique!'),
    ]
