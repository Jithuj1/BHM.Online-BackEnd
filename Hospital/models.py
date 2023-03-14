from django.db import models

# Create your models here.


class Hospitals(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    category = models.CharField(max_length=255)
    blood = models.BooleanField(default=True)
    image = models.FileField(upload_to='Image/Hospital/', null=True)
