from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import EmployeesViewSet



router = routers.DefaultRouter()
router.register('list', EmployeesViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
