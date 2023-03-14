import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .serializers import ChatMessageSerializer
from rest_framework.response import Response
from . models import ChatMessage,ChatRoom
from channels.db import database_sync_to_async






class TextRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        # Leave room group
       await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_msg(self,data):
        sender = data['sender']
        print('sender111',sender)
        message = data['message']
        print('message',message)
        room = data['room']
        print('rrrrrmmmm',room)
        print('text',data)
        # created_at = data['createdAt']
        roo = ChatRoom.objects.get(id=room)
        print('room no',roo)
        self. messages = ChatMessage.objects.create(sender=sender,message=message,room=roo)
        return  self.messages 
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = data['sender']
        print('sender111',sender)
        message = data['message']
        print('message',message)
        room = data['room']
        print('rrrrrmmmm',room)
        print('text',text_data)
        # created_at = data['createdAt']
        # roo = ChatRoom.objects.get(id=room)
        # print('room no',roo)
        # messages = ChatMessage.objects.create(sender=sender,message=message,room=roo)
        # print('attri',messages)
        msg = await self.save_msg(data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                # 'sender': sender
            }
        )
    
        
        
        
    async def chat_message(self,event):
        # Receive message from room group
        text = event['message']
        print('text1',text)
        # sender = event['sender']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': text,
            # 'sender': sender
    }))