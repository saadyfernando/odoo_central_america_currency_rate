# odoo_api_currency_rate

### Esta es la primera y única opción actualmente que ofrece actualización de Tasas de Cambio del dólar con las conversiones oficiales de la banca nacional y bancos centrales de Guatemala, Honduras, Nicaragua y Costa Rica

### Este módulo permite actualizar la tasa de cambio del día de las siguientes monedas con respecto al USD consumiendo la API de conversiones proporcionada por <a target="_blank" href="https://webs.hn/exchengerate-api/">webs.hn</a>: 

🇬🇹 Guatemala - Quetzal (GTQ)<br>
🇭🇳 Honduras - Lempira (HNL)<br>
🇳🇮 Nicaragua - Córdoba (NIO)<br>
🇨🇷 Costa Rica - Colón (CRC)<br>

### Una vez instalado el módulo debe configurar las Monedas a actualizar la tasa de cambio, así como los datos de acceso a la API. Esta Opción se encuentra en: 

Contabilidad / Configuración / Ajustes / Monedas. (Odoo Enterprise)<br>
Facturación y Contabilidad / Configuración / Ajustes / Monedas. (Odoo Community)

<img src="https://webs.hn/wp-content/uploads/2023/06/Captura-de-pantalla-2023-06-24-a-las-3.18.51-p.-m.png">

### Acción planificada que se encargará de realizar la actualización de forma automática. Esta Opción se encuentra en:

Ajustes / Técnico / Automatización / Acciones planificadas. (Modo desarrollador activo)

<img src="https://webs.hn/wp-content/uploads/2023/06/Captura-de-pantalla-2023-06-24-a-las-3.22.47-p.-m.png">
⚠️ Se recomienda periodo de actualización de 30 minutos o menos.

### Visualización en monedas de las tasas actualizadas:

Contabilidad / Configuración / Monedas. (Odoo Enterprise)<br>
Facturación y Contabilidad / Configuración / Monedas. (Odoo Community)

