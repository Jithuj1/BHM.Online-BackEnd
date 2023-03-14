# chat/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<int:room_name>/<int:sender>/", consumers.ChatConsumer.as_asgi()),
]
