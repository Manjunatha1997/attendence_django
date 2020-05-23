from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from mca.forms import *
from django.contrib import messages
from leave.models import *
from leave.forms import *
# Create your views here.

def index(request):
    return  render(request,'mca/index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')