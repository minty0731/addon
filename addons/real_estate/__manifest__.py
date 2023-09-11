{
    'name': 'Real Estate Advertisement',
    'version': '1.0',
    'category': 'Real Estate',
    'description': 'Manage Real Estate Advertisements',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
                'views/estate_property_views.xml',
                'views/estate_menus.xml',
                'views/estate_property_type_views.xml',
                'views/estate_property_tag_views.xml',
                'views/estate_property_offer_views.xml',
                'views/res_users_views.xml',
                ],  
    'demo': [],  
    'installable': True,
    'auto_install': False,

}