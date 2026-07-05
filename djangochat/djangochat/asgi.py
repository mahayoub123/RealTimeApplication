import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # WebSocket configuration can be added here once the 'room' app routing is implemented:
    # "websocket": AuthMiddlewareStack(
    #     URLRouter(
    #         room.routing.websocket_urlpatterns
    #     )
    # )
})

