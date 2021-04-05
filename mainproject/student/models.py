from django.db import models
from datetime import datetime,date

# Create your models here.
class student(models.Model):
    state=models.CharField(max_length=10)
    fname=models.CharField(max_length=10)
    sname=models.CharField(max_length=20)
    cno=models.IntegerField()
    bbb=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    email=models.EmailField(max_length=20)
    password=models.IntegerField()
    gender=models.CharField(max_length=5)
    add=models.CharField(max_length=40)
    black=models.CharField(max_length=5)
    course=models.CharField(max_length=5)
    icetpie=models.ImageField(upload_to="icet")
    image=models.ImageField(upload_to="photos")
    dname=models.CharField(max_length=30)
    du=models.CharField(max_length=10)
    dyop=models.IntegerField()
    dtm=models.IntegerField()
    iname=models.CharField(max_length=30)
    iu=models.CharField(max_length=10)
    iyop=models.IntegerField()
    itm=models.IntegerField()
    ssname=models.CharField(max_length=30)
    su=models.CharField(max_length=10)
    syop=models.IntegerField()
    stm=models.IntegerField()

    
    

