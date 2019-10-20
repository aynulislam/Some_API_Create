
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from empapp_1 import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Designation/', views.DesignationAPIView.as_view(), name='Designation-'),
    path('Employee/', views.EmployeeAPIView.as_view(), name='Employee-list'),
    path('designationupdate/', views.designationupdate.as_view(), name='designation_update'),

]




