from odoo import models, fields, api, exceptions
from datetime import date, timedelta
from odoo.tools import float_utils

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=(date.today() + timedelta(days=90)).strftime('%Y-%m-%d') 
    )
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)  
    living_area = fields.Integer(string="Living Area (sq m)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sq m)")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    active = fields.Boolean(string='Active', default=True)
    
    state = fields.Selection(
        [('new', 'New'), 
         ('offer_received', 'Offer Received'), 
         ('offer_accepted', 'Offer Accepted'), 
         ('sold', 'Sold'), 
         ('canceled', 'Canceled')],
        string='Status',
        required=True,
        copy=False,
        default='new'
    ) 
    
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    
    
    total_area = fields.Float(compute="_compute_total_area", string="Total Area")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson_id = fields.Many2one('res.users', string="Salesperson", default=lambda self: self.env.user, required=True)
    
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='Status', required=True, copy=False, default='new')
    
    def action_cancel(self):
        if self.state == 'sold':
            raise exceptions.UserError("A sold property cannot be canceled.")
        self.state = 'canceled'

    def action_sold(self):
        if self.state == 'canceled':
            raise exceptions.UserError("A canceled property cannot be set as sold.")
        self.state = 'sold'
    
    @api.onchange('salesperson_id')
    def _onchange_salesperson_id(self):
        if self.salesperson_id:
            self.buyer_id = self.salesperson_id.partner_id.id

    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = False
            self.garden_orientation = False

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if not float_utils.float_is_zero(record.selling_price, precision_digits=2):  # Check if selling price is not zero
                min_selling_price = 0.9 * record.expected_price
                if float_utils.float_compare(record.selling_price, min_selling_price, precision_digits=2) == -1:  # Check if selling price is less than 90% of expected price
                    raise exceptions.ValidationError('The selling price cannot be less than 90% of the expected price!')

    _sql_constraints = [
        ('expected_price_check', 'CHECK(expected_price > 0)', 'The expected price must be strictly positive!'),
        ('selling_price_check', 'CHECK(selling_price >= 0)', 'The selling price must be positive!'),
    ]
