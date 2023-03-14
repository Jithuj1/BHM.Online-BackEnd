# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from .serializers import MessageSerializer
from .models import Messages, Rooms
from Patient.models import Patient
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
    )

        await self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )


    @database_sync_to_async
    def saveMessage(self, data):
        print('inside')
        message = data['message']
        sender = data['sender']
        room_id = self.room_name
        msg = Messages()
        msg.room_name = Rooms.objects.get(id = room_id)
        msg.sender = Patient.objects.get(id = sender) 
        msg.content = message
        msg.save()



    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        msg = await self.saveMessage(text_data_json)

        await self.channel_layer.group_send( 
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': text_data_json['sender']
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': event['sender']
        }))