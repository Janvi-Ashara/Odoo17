from odoo import models, fields ,_
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_urgent = fields.Boolean(string="Urgent", default=False, help="Mark this purchase as urgent")

    def button_confirm(self):
        limit_amount = 50000  # ₹50,000 limit

        for order in self:
            if order.amount_total > limit_amount:
                # Check if the current user is not a Purchase Manager
                if not self.env.user.has_group('purchase.group_purchase_manager'):
                    raise UserError(_(
                        "You cannot confirm this Purchase Order because its total "
                        "amount is above ₹{0}. Please contact a Purchase Manager."
                    ).format(limit_amount))

            # If check passes, continue normal confirmation
        return super(PurchaseOrder, self).button_confirm()
