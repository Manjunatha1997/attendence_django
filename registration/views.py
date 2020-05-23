from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from registration.forms import LoginForm
from django.contrib import messages
# Create your views here.

def index(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=  form.cleaned_data['username']
            password =  form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                # if username == 'majnu':
                if user.is_superuser:
                    login(request,user)
                    return redirect('/mca/')
                else:
                    login(request,user)
                    return redirect('/student/')
            else:
                messages.error(request,'invalid credentials')


    return render(request,'registration/index.html',{'form':form})

