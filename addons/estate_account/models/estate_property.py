from odoo import models, api

class EstatePropertyInherited(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        for record in self:
            # 6% of the selling price
            six_percent_amount = 0.06 * record.selling_price

            # invoice lines
            invoice_line_data = [
                (0, 0, {
                    'name': '6% Commission',
                    'quantity': 1,
                    'price_unit': six_percent_amount,
                }),
                (0, 0, {
                    'name': 'Administrative Fees',
                    'quantity': 1,
                    'price_unit': 100.00,
                })
            ]

            # Create an invoice for the current estate property 
            invoice_vals = {
                'partner_id': record.buyer_id.id,  
                'move_type': 'out_invoice',    
                'invoice_line_ids': invoice_line_data
            }
            self.env['account.move'].create(invoice_vals)

        return super(EstatePropertyInherited, self).action_sold()
