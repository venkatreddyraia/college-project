from django.db import models
from datetime import datetime,date

# Create your models here.
class college(models.Model):
    idno=models.IntegerField()
    name=models.CharField(max_length=20)
    father=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    cno=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=20)
    password=models.IntegerField()
    exp=models.IntegerField()
    qul=models.CharField(max_length=10)
    select=models.CharField(max_length=10)
    doo=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    djj=models.IntegerField(default=False)

   

