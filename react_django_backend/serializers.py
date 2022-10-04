from rest_framework import serializers
from .models import User
from .models import Employee
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'role', 'email', 'contact', 'password', 'isActive']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'address', 'role', 'email', 'contact', 'password', 'isActive']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_caption', 'user_id', 'status']