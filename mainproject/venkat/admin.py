from django.contrib import admin
from college.models import college
from student.models import student

# Register your models here.
admin.site.register(college)
admin.site.register(student)