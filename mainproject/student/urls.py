from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.home),
    path('about',views.about,name="about"),
    path('course' ,views.course,name="course"),
    path('images',views.images,name="images"),
    path('icet',views.icet,name="icet"),
    path('studentreg',views.registration,name="studentreg"),
    path('faculty',views.faculty,name="faculty"),
    path('mcafaculty', views.mcafaculty,name="mcafaculty"),
    path('mbafaculty',views.mbafaculty,name="mbafaculty"),
    path('stulogin',views.stulogin,name="stulogin"),
    path('studentview',views.studentview,name="studentview"),
    path('stushow',views.stushow,name="stushow"),
    path('contact',views.contact,name="contact")
]