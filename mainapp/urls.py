from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import home,profile,addPatient,editpatient,searchpatient,addvisitdetail,visitdetails


urlpatterns = [
    path('', home ),
    path('accounts/login/', LoginView.as_view(template_name="login.html"),name="login" ),
    path('accounts/registration/', LoginView.as_view(),name="registration" ),
    path('accounts/profile/', profile ,name="profile" ),
    path('accounts/addpatient/', addPatient ,name="addpatient" ),
    path('accounts/editpatient/<pk>/', editpatient ,name="editpatient" ),
    path('accounts/searchpatient/', searchpatient ,name="searchpatient" ),
    path('accounts/addvisitdetail/<pk>/',addvisitdetail,name="addvisitdetail"),
    path('accounts/visitdetail/<pk>/',visitdetails, name="visitdetail"),
]