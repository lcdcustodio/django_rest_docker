from rest_framework import viewsets, status
from .models import Employees
from .serializers import EmployeesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
