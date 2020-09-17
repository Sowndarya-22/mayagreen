from django.urls import path
from .import views

urlpatterns=[
    
    #path('',views.home,name="home"),
    path('',views.webpage,name="webpage"),
    path('next/',views.next,name="next"),
    #path('role/',views.role,name="role"),    
    
    
    
    ]