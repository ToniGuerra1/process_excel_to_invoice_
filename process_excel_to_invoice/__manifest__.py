# -*- coding: utf-8 -*-
{
    'name': 'Import SaleOrder COD Reference',
    'version': '1.0',
    'author': 'Toni Guerra',
    'category': 'Sales',
    'summary': 'Wizard para cargar referencia COD en sale.order desde Excel',
    'license': 'OPL-1',
    'price': 49.00,
    'currency': 'EUR',
    'description': """
Este módulo agrega un wizard para subir un XLSX con números de pedido (sale.order),
y actualizar un campo 'sale_ref_cod' con la referencia COD digitada por el usuario.
""",
    'depends': [
        'sale',    # necesitamos 'sale.order'
        'account',  # solo si necesitamos el menú "menu_account_actions"
        'base'
    ],
    'data': [
        # La vista del wizard
        'views/import_saleorder_cod_wizard_views.xml',
        'security/ir.model.access.csv'
        # La vista que hereda sale.order para mostrar sale_ref_cod
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
