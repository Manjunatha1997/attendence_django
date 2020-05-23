from django.urls import path
from student.views import *
urlpatterns = [
    path('',index),
    path('attendResult/<int:user>/',attendResult),
    path('logout/',logout),

]