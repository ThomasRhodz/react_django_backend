from django.contrib import admin
from .models import User
from .models import Employee
from .models import Post

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Post)