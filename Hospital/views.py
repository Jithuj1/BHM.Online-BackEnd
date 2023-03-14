from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Hospitals
from .serializer import HospitalSerializer
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

@api_view(['GET', 'POST'])
def hospital(request):
    if request.method == "GET":
        doctors = Hospitals.objects.all()
        serializer = HospitalSerializer(doctors, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        print("datas", request.data)
        serializer = HospitalSerializer(data ={'name':request.data['name'], 'phone':request.data['phone'],
        'email':request.data['email'],'address':request.data['address'],'blood':request.data['blood'],'category':request.data['category'],'image':request.data['image']})
        name = request.data.get('name')
        print(serializer.is_valid())
        print("jithu", serializer.errors)
        dept = Hospitals.objects.filter(name=name)
        if dept:
            return Response("already")
        else:
            print("inside")
            if serializer.is_valid():
                # print(type(request.data['image']))
                # print("jjjj",serializer['image'])
                serializer.save()
                
                return Response({"status":status.HTTP_202_ACCEPTED, "status":"ok" })
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['PUT', 'DELETE'])
def update(request, id):
    if request.method == 'DELETE':
        dept = Hospitals.objects.filter(id = id)
        if dept:
            dept.delete()
            return Response("deleted")
        else:
            return Response("not found")