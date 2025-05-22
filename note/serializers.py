from rest_framework import serializers
from .models import danshjo
from .models import notebock
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = danshjo 
        fields = '__all__'
class Student2Serializer(serializers.ModelSerializer):
    class Meta:
        model = notebock
        fields = '__all__'