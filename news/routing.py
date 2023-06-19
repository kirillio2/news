from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    'websovket': AuthMiddlewareStack(
        URLRouter(
            # chat.routing.websocket_urlpatterns
        )
    ),
})