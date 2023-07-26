# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    currencies_ids = fields.Many2many('res.currency', related='company_id.currencies_ids', string='Currencies',
                                      domain='[("active","=",True)]', readonly=False)
    api_url = fields.Char(string='Url', related='company_id.api_url', readonly=True,
                          default='https://exchangerate.webs.hn/api/latest/?key=')
    api_key = fields.Char(related='company_id.api_key', string='Key', readonly=False)
    api_request_web = fields.Char(string='Api Request', readonly=True, related='company_id.api_request_web')
