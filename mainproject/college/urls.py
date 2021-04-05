from django.urls import path,include
from college import views

urlpatterns = [
    path('',views.clogin,name="clogin"),
    path('copen',views.copen,name="copen"),
    path('csingup',views.csingup,name="csignup"),
    path('cshow',views.cshow, name="cshow"),
    path('ok',views.ok,name="ok"),
    path('logout',views.logout,name="logout")
]