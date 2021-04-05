from django.shortcuts import render
from college import views
from college.models import college

# Create your views here.
def clogin(request):
    return render(request,"clogin.html")
def copen(request):
     em= request.POST["username"]
     password = request.POST['password']
     try:
        res = college.objects.get(email=em,password=password)
        response=render(request, "copen.html", {"message": res})
        return response
     except college.DoesNotExist:
        return render(request,'clogin.html',{'data':"invalid user"})
   
def csingup(request):
    return render(request,"csignup.html")
def cshow(request):
    name=request.POST.get("name")
    father=request.POST.get("father")
    city=request.POST.get("city")
    cno= request.POST.get("cno")
    doo=request.POST.get("doo")
    djj=request.POST.get("djj")
   
    email=request.POST.get("email")
    password=request.POST.get("password")
    qul=request.POST.get("qul")
    exp=request.POST.get("exp")
    select=request.POST.get("select")
    e={"name":name,"father":father,"city":city,"cno":cno,"doo":doo,"djj":djj,
    "email":email,"password":password,"qul":qul,"exp":exp,"select":select}
    info=college(name=name,father=father,city=city,cno=cno,doo=doo,djj=djj,
    qul=qul,exp=exp,select=select,email=email,password=password)
    info.save()
    return render(request,"cshow.html",e)
    
def ok(request):
    return render(request,"home.html")
def logout(request):
    return render(request,"clogin.html")