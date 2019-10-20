from django import views
from .views import DesignationAPIView, EmployeeAPIView
from django.urls import path

urlpatterns = [
    path('Designation/', DesignationAPIView, name="Designation"),
    path('Employee/<int:pk>', EmployeeAPIView, name="Employee"),



]
