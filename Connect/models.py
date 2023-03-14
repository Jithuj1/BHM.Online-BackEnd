from django.db import models
from Patient.models import Patient

# Create your models here.


class Rooms(models.Model):
    room_name = models.CharField( max_length=255, null=True)
    sender = models.ForeignKey(Patient, related_name='Right', on_delete=models.CASCADE, null= True)
    receiver = models.ForeignKey(Patient, related_name='Left', on_delete=models.CASCADE, null= True)
    videoId = models.IntegerField(default=6789)


class Messages (models.Model):
    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    sender = models.ForeignKey(Patient, on_delete=models.CASCADE)
    content = models.TextField()


class Notification(models.Model):
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True, null=True)
    now = models.DateTimeField(auto_now=True, null=True)
    patient = models.ForeignKey(Patient, related_name='notification_sender', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Patient, related_name='notification_receiver', on_delete=models.CASCADE)
    read = models.BooleanField(default=False, null=True)
