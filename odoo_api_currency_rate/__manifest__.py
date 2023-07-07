# -*- coding: utf-8 -*-
{
    'name': "Precio del dólar - Centroamérica (Banca nacional)",
    'summary': """
        Permite la actualización de Tasas de cambio de las siguientes monedas con respecto al USD
            1. Guatemala - Quetzal
            2. Honduras - Lempira
            3. Nicaragua - Córdoba
            4. Costa Rica - Colón
        """,
    'category': 'Accounting/Accounting',
    'version': '0.1',
    'depends': ['account', 'mail'],
    'author': "webs.hn",
    'license': 'LGPL-3',
    'data': [
        'data/data.xml',
        'data/channel.xml',
        'data/cron.xml',
        'views/res_config_settings_views.xml',

    ],
    'images': [
        'static/description/icon.png',

    ],
    'sequence': 0,

}
