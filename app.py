"""
app.py
------
Punto de entrada de la aplicación Flask.
"""

from flask import Flask, render_template
import config
from data.products import products

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        products=products,
        brand_name=config.BRAND_NAME,
        slogan=config.SLOGAN,
        whatsapp_number=config.WHATSAPP_NUMBER,
        social_links=config.SOCIAL_LINKS,
        schedule=config.SCHEDULE,
        delivery_zone=config.DELIVERY_ZONE,
        site_title=config.SITE_TITLE,
        site_description=config.SITE_DESCRIPTION,
    if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=port)






