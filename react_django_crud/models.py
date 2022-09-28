from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isActive  = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' - ' + self.role