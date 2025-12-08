from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = get_wsgi_application()

# Este nombre es obligatorio para Vercel
def handler(event, context):
    return app(event, context)
