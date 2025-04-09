from pathlib import Path

# Crear el contenido del README.md
readme_content = """# 📄 Process Excel to Invoice (Módulo Odoo)

Convierte archivos Excel en facturas dentro de Odoo con un solo clic. Automatiza la importación de pedidos y genera facturas directamente desde un archivo `.xlsx`.

---

## 🤖 ¿Qué es este módulo?

El módulo **Process Excel to Invoice** permite:

- Buscar pedidos (`sale.order`) por nombre desde una columna del archivo Excel.
- Asignar referencias de pago personalizadas.
- Crear facturas automáticamente si se desea.
- Actualizar el campo `payment_reference` en todas las facturas relacionadas.

---

## 📊 Beneficios Clave

✅ Automatización masiva desde Excel  
✅ No requiere conocimientos técnicos  
✅ Integración total con Odoo (sale.order y facturas)  
✅ Compatible con archivos Excel y exportaciones de Google Sheets

---

## ⚙️ Funcionalidades Destacadas

### 🔹 Importación masiva desde Excel (.xlsx)

- Selecciona la columna con el número de pedido
- Asigna referencias y crea facturas automáticamente

### 🔹 Creación de facturas opcional

- Marca “Crear Factura” en el asistente
- Si no existe una factura, se crea y valida desde código

### 🔹 Interfaz intuitiva

- Asistente simple paso a paso
- Vista con resultados claros y logs dentro de Odoo

---

## 🧪 Casos de Uso Reales

- Importación de pedidos desde tiendas externas (Amazon, Shopify, etc.)
- Inclusión de referencias de pago externas para conciliaciones
- Automatización de facturación desde reportes logísticos

---

## 💬 Testimonios

> “Ideal para pasar de Excel a ERP. Nos ahorra horas de trabajo manual cada semana.” — Operador logístico

> “Con una sola plantilla de Excel, cargamos todas las referencias de pago en minutos.” — Responsable de facturación

---

## 💸 Precio del Módulo

💶 **49 € (pago único)**

Incluye:
- Acceso completo al módulo
- Soporte por email
- Actualizaciones gratuitas
- Compatible con **Odoo 17**

---

## 📥 Enlaces

👉 [Comprar ahora]  
📞 [Solicitar demo]  
📚 [Ver documentación]

---

## 🛠️ Instalación

1. Extrae el módulo en tu carpeta de addons personalizados.
2. Reinicia el servidor de Odoo.
3. Ve a **Apps > Actualizar lista**.
4. Busca "Process Excel to Invoice" e instálalo.

---

## 📄 Licencia

Este módulo está licenciado bajo **OPL-1** (Odoo Proprietary License v1.0).

- Uso permitido en **una única base de datos**.
- Prohibida su redistribución o modificación sin permiso.
- El módulo se ofrece **“tal cual”**, sin garantía de funcionamiento.
"""

# Crear el contenido del LICENSE.txt
license_content = """Copyright © 2024 Toni (Cannactiva)

This software and associated files (the "Software") may only be used 
(executed, modified, executed after modifications) if you have 
purchased a valid license from the publisher.

The above permissions are granted for a single database per purchased 
license. 

This license does not allow you to distribute, sublicense, or sell 
copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
"""

# Guardar los archivos
readme_path = Path("/mnt/data/README.md")
license_path = Path("/mnt/data/LICENSE.txt")

readme_path.write_text(readme_content, encoding="utf-8")
license_path.write_text(license_content, encoding="utf-8")

readme_path, license_path
