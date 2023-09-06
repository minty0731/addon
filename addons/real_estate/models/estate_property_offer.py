from odoo import api, fields, models, exceptions

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string="Offer Price", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', required=True, copy=False, default='new')

    def action_accept(self):
        if self.property_id.state == 'sold':
            raise exceptions.UserError("This property has already been sold!")
        
        self.property_id.buyer_id = self.partner_id
        self.property_id.selling_price = self.price
        self.property_id.state = 'sold'
        self.state = 'accepted'
        
        other_offers = self.search([('property_id', '=', self.property_id.id), ('id', '!=', self.id)])
        other_offers.write({'state': 'refused'})

    def action_refuse(self):
        self.state = 'refused'

    _sql_constraints = [
        ('offer_price_check', 'CHECK(price > 0)', 'The offer price must be strictly positive!'),
    ]
