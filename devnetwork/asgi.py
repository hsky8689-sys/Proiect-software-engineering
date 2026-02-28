"""
ASGI config for devnetwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websockets_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devnetwork.settings')
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http":django_asgi_app,
        "https":django_asgi_app,
        "websocket":AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websockets_urlpatterns))
        )
    }
)
