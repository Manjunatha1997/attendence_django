from django.shortcuts import render,redirect
from leave.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from mca.models import Student

@login_required(login_url='/')
def applyLeave(request):
    form = ApplyLeaveForm()

    # rollno = Student.objects.get(user=request.user)
    if request.method == 'POST':
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            # form.save()
            user = str(request.user) # getting current user...
            user = int(user)
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            reason = form.cleaned_data['reason']
            status = 'Pending'
            if ((end_date - start_date).days) <= 0:
                messages.error(request,'start date must be greater than end date')
            else:
                ApplyLeave.objects.create(rollno = user, start_date = start_date, end_date = end_date, reason = reason, status = status)
                messages.info(request,'leave applied successfully')
                return redirect('/leave/applyLeave/')
    else:
        form = ApplyLeaveForm()
    return render(request,'leave/applyLeave.html',{'form':form})

@login_required(login_url='/')
def leaveStatus(request,pk):
    all_data = ApplyLeave.objects.filter(rollno = pk)[::-1]

    return render(request,'leave/leaveStatus.html',{'all_data':all_data})


def checkLeaveApplied(request):
    all_data = ApplyLeave.objects.filter(status = 'Pending')
    # all_data = ApplyLeave.objects.all()

    return render(request,'leave/checkLeaveApplied.html',{'all_data':all_data})



def approved(request,pk):
    all_data = ApplyLeave.objects.filter(id = pk)
    for data in all_data:
        data.status = 'Approved'
        data.save()
    return redirect('/leave/checkLeaveApplied')


def canceled(request,pk):
    all_data = ApplyLeave.objects.filter(id = pk)
    for data in all_data:
        data.status = 'Canceled'
        data.save()
    return redirect('/leave/checkLeaveApplied')

