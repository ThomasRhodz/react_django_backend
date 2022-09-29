from django.http import JsonResponse
from .models import User
from .models import Employee
from .serializers import UserSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Basic CRUD for Users
@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'data': serializer.data})

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# With filters

def user_active(request):
    users = User.objects.filter(isActive='Yes')
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})

def user_inActive(request):
    users = User.objects.filter(isActive='No')
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'data': serializer.data})



# Basic CRUD for Employees
@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse({'data': serializer.data})

    if request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
    
    try:
        employee = Employee.objects.get(pk=id)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# With filters

def employee_active(request):
    employees = Employee.objects.filter(isActive='Yes')
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({'data': serializer.data})

def employee_inActive(request):
    employees = Employee.objects.filter(isActive='No')
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({'data': serializer.data})