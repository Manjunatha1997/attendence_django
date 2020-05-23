from django.shortcuts import render,redirect
from firstyear.models import Attend as FAttend
from secondyear.models import Attend as SAttend
from thirdyear.models import Attend as TAttend
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def index(request):
    return render(request,'student/index.html')


@login_required(login_url='/')
def attendResult(request,user):
    fall_data = FAttend.objects.filter(rollno=user)
    sall_data = SAttend.objects.filter(rollno=user)
    tall_data = TAttend.objects.filter(rollno=user)
    return render(request,'student/attendResult.html',{'fall_data':fall_data,'sall_data':sall_data,'tall_data':tall_data})


def logout(request):
    auth.logout(request)
    return redirect('/')