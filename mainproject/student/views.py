from django.shortcuts import render
from student import views
from student.models import student
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def course(request):
    return render(request,"course.html")
def images(request):
    return render(request,"images.html")
def icet(request):
    return render(request,"icet.html")
def registration(request):
    ii=request.POST.get("icet")
    if ii=="1234":
        return render(request,"studentreg.html")
    else:
        return render(request,"icet.html",{"error":"invlid detailes"})
def faculty(request):
    return render(request,"faculty.html")
def mcafaculty(request):
    return render(request,"mcafaculty.html")
def mbafaculty(request):
    return render(request,"mbafaculty.html")
def stulogin(request):
    return render(request,"stulogin.html")
def studentview(request):
    state=request.POST.get("state")
    fname=request.POST.get("fname")
    sname=request.POST.get("sname")
    cno=request.POST.get("cno")
    bbb=request.POST.get("bbb")
    email=request.POST.get("email")
    password=request.POST.get("password")
    gender=request.POST.get("gender")
    black=request.POST.get("black")
    add=state=request.POST.get("add")
    course=request.POST.get("course")
    icetpie=request.FILES["icetpie"]
    image=request.FILES["image"]
    dname=request.POST.get("dname")
    du=request.POST.get("du")
    dyop=request.POST.get("dyop")
    dtm=request.POST.get("dtm")
    iname=request.POST.get("iname")
    iu=request.POST.get("iu")
    iyop=request.POST.get("iyop")
    itm=request.POST.get("itm")
    ssname=request.POST.get("ssname")
    su=request.POST.get("su")
    syop=request.POST.get("syop")
    stm=request.POST.get("stm")
    venkat={"state":state,"fname":fname,"sname":sname,"cno":cno,"bbb":bbb,"email":email,"password":password,
    "gender":gender,"black":black,"add":add,"course":course,"icetpie":icetpie,"image":image,"dname":dname,
    "du":du,"dyop":dyop,"dtm":dtm,"iname":iname,"iu":iu,"iyop":iyop,"itm":itm,"ssname":ssname,
    "su":su,"syop":syop,"stm":stm}
    sreg=student(state=state,fname=fname,sname=sname,cno=cno,bbb=bbb,email=email,password=password,
    gender=gender,black=black,add=add,course=course,icetpie=icetpie,image=image,dname=dname,du=du,
    dyop=dyop,dtm=dtm,iname=iname,iu=iu,iyop=iyop,itm=itm,ssname=ssname,su=su,syop=syop,stm=stm)
    sreg.save()
    return render(request,"stushow.html",venkat)
def stushow(request):
     emm= request.POST["susername"]
     passwords = request.POST["spassword"]
     try:
        res = student.objects.get(email=emm,password=passwords)
        response=render(request, "stuview.html", {"message": res})
        return response
     except student.DoesNotExist:
        return render(request,'stulogin.html',{'data':"invalid user"})
def contact(request):
    return render(request,"contact.html")

    