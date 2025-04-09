# -*- coding: utf-8 -*-
{
    'name': 'Process Excel to Invoice',
    'version': '1.0',
    'author': 'Toni Guerra',
    'category': 'Sales',
    'summary': 'Wizard to load payment reference into sale.order from Excel and choose whether to create the invoice directly.',
    'license': 'OPL-1',
    'price': 9.90,
    'currency': 'EUR',
    'description': """
📑 Import Payment Reference from Excel

Este módulo permite importar referencias de pago externas desde un archivo Excel y actualizarlas en tus pedidos de venta (sale.order) de forma masiva y sin necesidad de programación.

🔧 ¿Qué hace este módulo?
- Busca pedidos por nombre desde un archivo Excel
- Actualiza el campo payment_reference
- Opcionalmente crea y valida la factura si no existe

📂 Estructura del archivo Excel esperada:
ORDER_NAME     PAYMENT_REF     CREATE_INVOICE
SO1234         XYZ-789         TRUE
SO5678         ABC-123         FALSE

🚀 Funcionalidades clave:
- Importación masiva desde archivos .xlsx
- Interfaz tipo asistente fácil de usar
- Actualización automática y sin errores manuales
- Registro en logs de Odoo

💡 Casos de uso:
- Pedidos contra reembolso o transferencia
- Conciliación bancaria con referencias externas
- Integración con tiendas o sistemas externos

🧪 Requisitos:
- Archivo en formato .xlsx
- Nombre del pedido debe existir en Odoo

📄 Licencia:
Módulo bajo licencia OPL-1 (uso para una sola base de datos). No se permite redistribución ni modificación sin autorización. El módulo se entrega "tal cual", sin garantía.
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
