from django.urls import  path
from thirdyear.views import *

urlpatterns=[
    path('index/',index),
    path('addStudents/',addStudents),
    path('show/',show),
    path('attend/',attend),
    path('attendResult/',attendResult),
    path('searchResult/',searchResult),
    path('delete/<int:pk>/',delete),
    path('deleteStudent/<int:pk>/',deleteStudent),
    path('update/<int:pk>/',update),
    path('studentData/<int:pk>/',studentData),
    path('logout/',logout),

]