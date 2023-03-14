from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Patient(AbstractUser):
    age = models.IntegerField(null=False, default=25)
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=250, null=True)
    status = models.BooleanField(default=False)


class Appointment(models.Model):
    patient = models.ForeignKey("Patient.Patient", related_name= "patient_detail", on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor.Doctors", on_delete=models.CASCADE)
    department = models.ForeignKey("Doctor.Departments",  on_delete=models.CASCADE, null= True)
    hospital = models.ForeignKey("Hospital.Hospitals", on_delete=models.CASCADE, null= True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    section = models.CharField(max_length=50)
    status = models.BooleanField(default = False)