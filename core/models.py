from django.db import models

class Employees(models.Model):

    name = models.CharField(max_length=100, blank=False)
    workdept = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)

