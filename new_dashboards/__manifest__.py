# -*- coding: utf-8 -*-
{
    'name': "new dashboards",
    'summary': "Custom Sales & CRM Dashboards",
    'description': "Custom dashboards for Sales Orders, CRM, and Accounting.",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base', 'web', 'crm', 'sale', 'account', 'board'],

    'assets': {
        'web.assets_backend': [
            'new_dashboards/static/src/js/dashboard.js',
            'new_dashboards/static/src/js/sales_order.js',
            'new_dashboards/static/src/xml/dashboard.xml',
            'new_dashboards/static/src/xml/sale_dashboard.xml',

        ],
    },

    'data': [
        'views/views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
