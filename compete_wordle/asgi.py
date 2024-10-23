"""
ASGI config for compete_wordle project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from api.consumers import StandingsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compete_wordle.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:contest_id>/standings/', StandingsConsumer.as_asgi()),  # websocket_urlpatterns
        ])
    ),
})
