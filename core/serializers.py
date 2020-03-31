from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employees

# Serializers define the API representation.
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'name','workdept', 'title']
