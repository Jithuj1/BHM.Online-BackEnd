from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import RoomSerializer, MessageSerializer, NotificationSerializer, NotificationReadSerializer
from .models import Rooms, Messages, Notification
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.


@api_view(['POST'])
def RoomsData(request):
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    serializer = RoomSerializer(data= request.data)
    if serializer.is_valid():
        try:
            left = Rooms.objects.get(sender = sender, receiver = receiver)
            room_id = left.id
            return Response(data = room_id)
        except ObjectDoesNotExist:
            serializer.save()
            left = Rooms.objects.get(sender = sender, receiver = receiver)
            room_id = left.id
            return Response(data = room_id)

    

@api_view(['GET'])
def getRoom(request, patient, doctor):
    try:
        room = Rooms.objects.get(sender = patient, receiver = doctor)
        serializer = RoomSerializer(room)
        return Response(data = serializer.data)
    except:
            return Response(status= status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def UpdateRoom(request, id):
    try: 
        room = Rooms.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RoomSerializer(room, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(status= status.HTTP_200_OK)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
def singleMessages(request):
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    content = request.data.get('content')
    try:
        room = Rooms.objects.get(sender = sender, receiver = receiver)
        # room = Rooms.objects.get(receiver = sender, sender = receiver)
    except ObjectDoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer = MessageSerializer(data = {'room_name' : room.id, 'sender':sender, 'content':content })
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['POST', 'GET'])
def Notifications(request):
    if request.method == 'POST':
        uid = request.data['doctor']
        serializer = NotificationSerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_202_ACCEPTED)
        return Response(status= status.HTTP_406_NOT_ACCEPTABLE)
    else:
        notifications = Notification.objects.all().order_by('-id')
        serializer = NotificationReadSerializer(notifications, many=True)
        return Response({'status': status.HTTP_200_OK, 'data':serializer.data})
    

@api_view(['PUT'])
def updateNotification(request, id):
    try:
        singleNotification = Notification.objects.get(id = id)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer = NotificationSerializer(singleNotification, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(status= status.HTTP_202_ACCEPTED)
    return Response(status= status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def getMessage(request, id):
    msgs = Messages.objects.filter(room_name = id)
    serializer = MessageSerializer(msgs, many = True)
    return Response(data= serializer.data)