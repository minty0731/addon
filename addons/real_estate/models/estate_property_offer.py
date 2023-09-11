from odoo import api, fields, models, exceptions
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = 'price desc'

    price = fields.Float(string="Offer Price", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    property_type_id = fields.Many2one(related='property_id.property_type_id', string='Property Type', store=True)
    
    state = fields.Selection([
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', required=True, copy=False, default='new')  

    @api.model
    def create(self, vals):
        property = self.env['estate.property'].browse(vals['property_id'])
        if 'price' in vals and vals['price'] < property.highest_offer: 
            raise exceptions.UserError("The offer amount is lower than the existing highest offer.")
        property.state = 'offer_received'  
        return super(EstatePropertyOffer, self).create(vals)

    def action_accept(self):
        self.ensure_one()
        self.state = 'accepted'

    def action_refuse(self):
        self.ensure_one()
        self.state = 'refused'

    _sql_constraints = [
        ('offer_price_check', 'CHECK(price > 0)', 'The offer price must be strictly positive!'),
    ]
