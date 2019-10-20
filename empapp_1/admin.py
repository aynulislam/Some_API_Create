from django.contrib import admin

# Register your models here.
from . models import Designation
# To register this Article Model in our Admin interface
admin.site.register(Designation)


from . models import Employee
# To register this Article Model in our Admin interface
admin.site.register(Employee)

