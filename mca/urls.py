from django.urls import  path
from mca.views import *

urlpatterns=[
    path('',index),
    path('logout/',logout),

]