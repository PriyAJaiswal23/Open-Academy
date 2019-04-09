# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        This is am application that helps displays courses and their massrks""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Samso9ite",
    'website': "http://www.samso9itedigitals.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'
                ,'account'
                ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}