# Copyright 2024 Dani - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class ResPartner(models.Model):

    _inherit = 'res.partner'

    telefonodos = fields.Char(
        string = "Phone Work"
    )