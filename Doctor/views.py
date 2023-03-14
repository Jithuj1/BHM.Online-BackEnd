from django.shortcuts import render
from .models import Doctors, Departments, Schedule
from Patient.models import Patient
from Hospital.models import Hospitals
from .serializers import DoctorSerializer, DepartmentSerializer, ScheduleSerializer, DoctorWriteSerializer
from Patient.serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Patient.models import Appointment

# Create your views here.

@api_view(['GET', 'POST'])
def doctor(request):
    print("data", request.data)
    if request.method == "GET":
        doctors = Doctors.objects.all()
        serializer = DoctorSerializer(doctors, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializers = PatientSerializer(data=request.data)
        username1 = request.data.get('username', None)
        email = request.data.get('email', None)
        if Patient.objects.filter(username = username1 ).exists():
            return Response ('username')
        if Patient.objects.filter(email = email ).exists():
            return Response ('email')
        if serializers.is_valid():
            serializers.save()
        staff = Patient.objects.get(username = username1)
        staff_id = staff.id
        department=request.data['department']
        exp=request.data['experience']
        hospital=request.data['hospital']
        image=request.data['image']
        level="Senior"
        note=request.data['note']    
        serializer = DoctorWriteSerializer(data={'department':department,'experience':exp,'doctor_id':staff_id,'hospital':hospital, "level":level, "note":note, 'status':False, "image":image})

        if serializer.is_valid():
            serializer.save()
            print("here2", serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print('else')
            return Response({"status":status.HTTP_403_FORBIDDEN})


@api_view(['PUT', 'DELETE', 'GET'])
def update(request, id):
    try:
        print("id", id)
        doctor = Doctors.objects.get(id=id)
        user_id = doctor.doctor_id.id
        print(user_id)
    except doctor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("jjjj")
        serializer = DoctorSerializer(doctor)
        return Response (serializer.data)
    elif request.method =="PUT":
        serializer = DoctorSerializer(doctor, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, Status = 400)

    elif request.method == "DELETE":
        user = Patient.objects.get(id = user_id)
        if user:
            user.delete()
            return Response ("Deleted")
        else:
            return Response (status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def departments(request):
    if request.method == "GET":
        doctors = Departments.objects.all()
        serializer = DepartmentSerializer(doctors, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DepartmentSerializer(data = request.data)
        name = request.data.get('name')
        print(name)
        dept = Departments.objects.filter(name=name)
        if dept:
            return Response("already")
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({"status":status.HTTP_202_ACCEPTED, "status":"ok" })
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['PUT', 'DELETE'])
def dept(request, id):
    if request.method == 'DELETE':
        dept = Departments.objects.filter(id = id)
        if dept:
            dept.delete()
            return Response("deleted")
        else:
            return Response("not found")


@api_view(['GET', 'POST'])
def schedule(request):
    if request.method == "GET":
        doctors = Schedule.objects.all()
        serializer = ScheduleSerializer(doctors, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        print(request.data)
        serializer = ScheduleSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({"status":status.HTTP_202_ACCEPTED, "status":"ok" })
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
