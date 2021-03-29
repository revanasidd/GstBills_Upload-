from django.urls import path
from NewApp import views

urlpatterns = [
    path('',views.dashbord,name='dashbord'),
    path('input/',views.input,name='input'),
    path('inputdata/',views.inputdata,name='inpudata'),
]
