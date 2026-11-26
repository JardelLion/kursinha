{
    'name': 'Kursinha',
    'version': '1.0.0',
    'description': 'Kursinha Webhook Integration',
    'summary': """Kursinha Webhook Integration
                Enable Make payment in Odoo using Kursinha api linked by Webhook""",
    'author': 'Jardel Elias Bernardo',
    'website': 'https://github.com/JardelLion',
    'license': 'LGPL-3',
    'category': '',
    'depends': ['website_payment', 'payment'],
    "data":[
        "data/payment_method.xml",
        "data/payment_provider.xml",
      
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}