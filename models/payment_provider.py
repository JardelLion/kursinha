from odoo import fields, models


class PaymentProviderInherit(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(selection_add=[
        ('kursinha', 'Kursinha')
    ],ondelete={'kursinha': 'set default'})