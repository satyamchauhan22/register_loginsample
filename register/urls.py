
from django.urls import path
from . import views
urlpatterns = [path('',views.home),
               path('https://registerlogin11.herokuapp.com/register/',views.reg),
               path('https://registerlogin11.herokuapp.com/loggedin/',views.loggedin)
               ]