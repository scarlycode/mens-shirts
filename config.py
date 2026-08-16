"""
config.py
---------
Este archivo centraliza TODA la información que puede cambiar con el tiempo:
número de WhatsApp, redes sociales, horario, zona de entrega, etc.

Regla de oro: si un dato puede cambiar en el futuro (tu número, tus redes),
NO lo escribas directo en el HTML. Ponlo aquí, una sola vez.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# INFORMACIÓN DE LA MARCA
BRAND_NAME = "MEN'S SHIRTS"
SLOGAN = "Tu estilo. Tu actitud. Tu esencia."

# WHATSAPP
# Coloca tu número real en el archivo .env, NUNCA aquí directamente.
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER", "AQUI_COLOCARE_MI_NUMERO")

# REDES SOCIALES
SOCIAL_LINKS = {
    "instagram": "",
    "facebook": "",
    "tiktok": ""
}

# CONTACTO Y OPERACIÓN
SCHEDULE = "Lunes a Sábado, 10:00 am - 7:00 pm"
DELIVERY_ZONE = "Zona por definir"

# SEO
SITE_TITLE = "Men's Shirts | Playeras y gorras para hombre"
SITE_DESCRIPTION = (
    "Descubre Men's Shirts, una marca de moda masculina con playeras y "
    "gorras para diferentes estilos. Conoce nuestra colección y reserva "
    "tu pedido por WhatsApp."
)