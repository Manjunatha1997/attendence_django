from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from registration.views import index

urlpatterns = [
    path('',index),
    path('logout/',LogoutView.as_view()),

]