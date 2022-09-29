from django.db import models

# from react_django_backend.views import user_detail

class User(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isActive  = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' - ' + self.role

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isActive  = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + self.last_name + ' - ' + self.role

class Post(models.Model):
    post_caption = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)