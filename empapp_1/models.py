from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])




# Create your models here.
class Designation(models.Model):
    #designation_id = models.IntegerField(max_length=100)
    designation = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.designation


class Employee(models.Model):
    emp_name = models.CharField( max_length=100,null=False)
    #emp_id = models.CharField(max_length=50, blank = True, null = True)
    description = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=False)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)



    def __str__(self):
        return self.emp_name



