from rest_framework import serializers
from .models import Doctors, Departments, Schedule


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'department', 'experience', 'hospital', 'doctor_id', 'level', 'note', 'status', 'image']
        depth = 1


class DoctorWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'department', 'experience', 'hospital', 'doctor_id', 'level', 'note', 'status', 'image']
    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'name']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
