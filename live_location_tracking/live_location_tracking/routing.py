# live_location_tracking/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from tracking.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'http': URLRouter({
        # Other HTTP routes
    }),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
