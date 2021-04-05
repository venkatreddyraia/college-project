from django.shortcuts import render
from college.models import college
from student.models import student

# Create your views here.

def login(request):
    return render(request,"loh.html")
def open(request):
    use=request.POST.get("username")
    pas=request.POST.get("password")
    if use=="sathyam" and pas=="sai":
        return render(request,"open.html")
    else:
        
        return render(request,"loh.html" ,{"error":"involid"})

def flist(request):
     qs = college.objects.all()
     return render(request,"flist.html" ,{"data":qs})
def slist(request):
    qq = student.objects.all()
    return render(request,"slist.html",{"data":qq})

def supdateEmploeyee(request):
    uid = request.POST.get("update_id")
    #res = EmployeeModel.objects.filter(id=uid)
    res = student.objects.get(id=uid)
    return render(request,"supdate.html",{"data":res})

def supdate_emp(request):
    id = request.POST.get("u_id")
    na = request.POST.get("u_name")
    sname = request.POST.get("u_sname")
    bb=request.POST.get("u_data")
    co=request.POST.get("u_course")
    student.objects.filter(id=id).update(fname=na,sname=sname,bbb=bb,course=co)
    return slist(request)

def sdeleteEmployee(request):
    did = request.POST.get("del_id")
    student.objects.filter(id=did).delete()
    return slist(request)

def mbalist(request):


        nanni = student.objects.filter(black='MBA' )
        nanni1 = student.objects.filter(black='MBA',course='MCA' )
        return render(request,"mbalist.html",{"data":nanni,"data2":nanni1})
    



def mcalist(request):


    nanni = student.objects.filter(black='MCA' )
    return render(request,"mbalist.html",{"data":nanni})

