from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        if 'default_code' not in vals or not vals.get('default_code'):
            vals['default_code'] = self.env['ir.sequence'].next_by_code('product.code') or '/'
        return super(ProductProduct, self).create(vals)
