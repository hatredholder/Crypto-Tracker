import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import positions.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_proj.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(positions.routing.websocket_urlpatterns),
    },
)
