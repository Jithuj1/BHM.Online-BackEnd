from rest_framework import serializers
from .models import Patient, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'age', 'phone', 'address', 'email',  'username', 'password',  'last_login', 'is_superuser', 'is_staff', 'date_joined', 'status']

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    
class AppointmentSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        depth = 4