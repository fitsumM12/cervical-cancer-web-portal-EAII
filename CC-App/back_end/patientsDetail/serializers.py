from rest_framework import serializers
from .models import patientsDetail

from django.utils import timezone

class PatientsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientsDetail
        fields = '__all__'

    def create(self, validated_data):
        validated_data['record_date'] = timezone.now().date() 
        return super().create(validated_data)
