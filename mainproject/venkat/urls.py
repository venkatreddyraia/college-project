from django.urls import path,include
from venkat import views

urlpatterns = [
   
    path('',views.login),
    path('open', views.open,name="open"),
    path('flist',views.flist,name="flist"),
    path('slist',views.slist,name="slist"),
    path('supdate',views.supdateEmploeyee,name="supdate"),
    path('supdate_emp',views.supdate_emp,name="supdate_emp"),
    path('sdelete',views.sdeleteEmployee,name="sdelete"),
    path('mbalist',views.mbalist,name="mbalist"),
    path('mcalist',views.mcalist,name="mcalist"),
   
    
]