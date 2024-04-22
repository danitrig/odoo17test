# Copyright 2024 Dani - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    phone2 = fields.char (
        string = "Phone Work"
    )