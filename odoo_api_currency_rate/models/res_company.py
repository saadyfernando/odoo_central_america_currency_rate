# -*- coding: utf-8 -*-


from odoo import fields, models, api, _
import json
import urllib3
from datetime import *


class ResCompany(models.Model):
    _inherit = 'res.company'

    currencies_ids = fields.Many2many('res.currency', 'res_company_currencies_rel', 'company_id',
                                      'currency_id', string='Currencies', domain='[("active","=",True)]')

    api_url = fields.Char(string='Url', default='https://exchangerate.webs.hn/api/latest/?key=')

    api_key = fields.Char(string='Api')
    api_request_web = fields.Char(string='Api Request',
                                  default='http://webs.hn/exchengerate-api')

    @api.model
    def _cron_update_exchange_rates(self):
        companies = self.env['res.company'].search([])
        for company in companies:
            response = company._get_connect_to_api()
            for currency in company.currencies_ids:
                company._update_rate_by_currency(response, currency)

    def _get_connect_to_api(self):
        response = dict()
        #url_connect = self.api_url + self.api_key
        url_connect = str(self.api_url) + str(self.api_key)
        http = urllib3.PoolManager()
        try:
            request_response = http.request('POST',
                                            url_connect,
                                            headers={'Content-Type': 'application/json'})
        except urllib3.exceptions.HTTPError as ex:
            print(ex)
        if request_response:
            response = json.loads(request_response.data.decode('utf-8'))
        return response

    def _update_rate_by_currency(self, response, currency):
        if 'base' in response:
            new_rate = False
            currencies = response['currencies']
            if currency.name in currencies:
                rate_currency = float(currencies[currency.name])
                if rate_currency > 0:
                    channel_id = self.env.ref('l10n_hn_api_currency_rate.exchange_rate_channel')
                    new_rate = True
                    date_exchange = datetime.now()
                    if 'date' in response:
                        date_exchange = response['date']
                    res_currency_rate = self.env['res.currency.rate'].sudo().search(
                        [('name', '=', date_exchange), ('currency_id', '=', currency.id),
                         ('company_id', '=', self.id)])

                    if len(res_currency_rate) == 0:
                        self.env['res.currency.rate'].sudo().create({
                            'currency_id': currency.id,
                            'name': date_exchange,
                            'rate': rate_currency,
                            'company_id': self.id,
                        })
                    else:
                        res_currency_rate.rate = rate_currency
                        new_rate = False
                    if new_rate:
                        channel_id.message_post(
                            body="New rate updated the exchange rate with date %s and value %s." % (
                                date_exchange, rate_currency),
                            message_type='notification',
                            subtype_xmlid='mail.mt_comment',
                        )
                    else:
                        channel_id.message_post(
                            body="The exchange rate was updated with date %s and value %s." % (
                                date_exchange, rate_currency),
                            message_type='notification',
                            subtype_xmlid='mail.mt_comment',
                        )
