from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Employees

admin.site.unregister(User)
admin.site.unregister(Group)


class EmployeesAdmin(ModelAdmin):
    list_display = ('name', 'workdept', 'title')

admin.site.register(Employees, EmployeesAdmin)


