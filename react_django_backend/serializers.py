from rest_framework import serializers
from .models import User
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'role', 'email', 'contact', 'password', 'isActive']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        field = ['id', 'first_name', 'last_name', 'address', 'role', 'email', 'contact', 'password', 'isActive']