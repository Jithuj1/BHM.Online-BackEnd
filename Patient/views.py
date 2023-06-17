from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PatientSerializer, AppointmentSerializer, AppointmentSerializerRead
from. models import Patient, Appointment
from Doctor.models import Doctors
from django.views.generic.list import ListView
from django.conf import settings
from django.core.mail import send_mail
from .tasks import celery_worker


# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['name'] = user.first_name
        token['admin'] = user.is_superuser
        token['staff'] = user.is_staff
        token['status'] = user.status
        # ...
        if token:
            return token
        else:
            return Response("False")


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST'])
def patient(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        print(patients)
        serializer = PatientSerializer(patients, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PatientSerializer(data= request.data)
        username1 = request.data.get('username', None)
        email = request.data.get('email', None)
        if Patient.objects.filter(username = username1 ).exists():
            return Response ('username')
        if Patient.objects.filter(email = email ).exists():
            return Response ('email')
        if serializer.is_valid():
            print('inside')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"status":status.HTTP_403_FORBIDDEN})
            
    

@api_view(['PUT', 'DELETE', 'GET'])
def update(request, id):
    try:
        print("id", id)
        user = Patient.objects.get(id=id)
    except user.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PatientSerializer(user)
        return Response (serializer.data)
    elif request.method =="PUT":
        serializer = PatientSerializer(user, data= request.data, partial = True)
        if serializer.is_valid():
            print('inside')
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, Status = 400)
    elif request.method == "DELETE":
        user = Patient.objects.get(id = user.id)
        if user:
            user.delete()
            return Response ("Deleted")
        else:
            return Response (status=status.HTTP_404_NOT_FOUND)


class AppointmentListView(APIView):
    def get(self, request, format = None):
        appoint = Appointment.objects.all()
        serializer = AppointmentSerializerRead(appoint, many = True)
        return Response (serializer.data)

    def post(self, request, format = None):
        serializer = AppointmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            date = request.data['date']
            d1 = Patient.objects.get(id = request.data['patient'])
            d2 = Doctors.objects.get(id = request.data['doctor'])
            d3 = Patient.objects.get(id = d2.doctor_id.id)
            dock = d3.first_name
            patient = d1.first_name
            email = d3.email
            send_email_celery(date, dock, patient, email)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (status = status.HTTP_406_NOT_ACCEPTABLE)


def send_email_celery(date, dock, patient, email):
    subject = f"Congratulations {dock}"
    message = 'You have a new appointment request on'  
    email_from = settings.EMAIL_HOST_USER
    message = f"You have a new appointment request on {date} please kindly make a response to  {patient} thank you" 
    recipient_list = [email]
    print(email)
    send_mail(subject, message, email_from, recipient_list) 



class AppointmentListDetail(APIView):
    def get_object(self, id):
        try:
            return Appointment.objects.get(id = id)
        except:
            return 
    def put(self, request, id, format = None):
        appoint = self.get_object(id)
        serializer = AppointmentSerializer(appoint, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_202_ACCEPTED)
        return Response(status= status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id, format = None):
        appoint = self.get_object(id)
        appoint.delete()
        return Response(status= status.HTTP_200_OK)

