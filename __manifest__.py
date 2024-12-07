# -*- coding: utf-8 -*-
{
    'name': "Despacho de Gasolina",

    'summary': """
        Gestion de Estacion de Gasolinera Nitro Gas para el Curso de Odoo""",

    'description': """
        Modulo para la Gestion de Estacion de Gasolinera Nitro Gas El Salvador
    """,

    'author': "MR Gomez",
    'website': "https://mrgomezsv.github.io/",

    'category': 'Services',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'reports/report_ticket.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
