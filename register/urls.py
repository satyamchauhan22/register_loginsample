
from django.urls import path
from . import views
urlpatterns = [path('',views.home),
               path('register/',views.reg),
               path('loggedin/',views.loggedin)
               ]