from django.db import models

# Create your models here.




class Departments(models.Model):
    name = models.CharField(max_length=255)

class Doctors (models.Model):
    department = models.ForeignKey(Departments, related_name= "dept", on_delete=models.CASCADE,null=True)
    hospital = models.ForeignKey("Hospital.Hospitals", related_name="working", on_delete=models.CASCADE,null=True)
    experience = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    note1 = models.CharField(max_length=255)
    note2 = models.CharField(max_length=255) 
    note3 = models.CharField(max_length=255)
    note4 = models.CharField(max_length=255)
    doctor_id = models.ForeignKey("Patient.Patient", related_name="doctor_details", on_delete=models.CASCADE,null=True)
    status = models.BooleanField(default=False)
    image = models.FileField(upload_to='Image/Doctors/', null=True)



class Schedule(models.Model):
    doctor = models.ForeignKey(Doctors, related_name="dock", on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    start = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    end = models.TimeField(auto_now=False, auto_now_add=False, null=False)


    