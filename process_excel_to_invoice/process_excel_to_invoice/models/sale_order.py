from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_reference_to_invoice = fields.Char(string="Payment reference to invoice")
