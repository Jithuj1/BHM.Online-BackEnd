from rest_framework import serializers
from .models import Hospitals


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = "__all__"
        # read_only_fields = ['id'] 


    