from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from thirdyear.forms import *
from django.contrib import messages
from leave.models import *
from leave.forms import *
# Create your views here.

def index(request):
    return  render(request,'thirdyear/index.html')

def addStudents(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            rollno = form.cleaned_data['rollno']
            name = form.cleaned_data['name']
            password = form.cleaned_data['phno']

            User.objects.create_user(first_name = name,username = rollno, password = password)

            return redirect('/thirdyear/addStudents/')

    return render(request,'thirdyear/addStudents.html',{'form':form})

def show(request):
    all_data = Student.objects.all()
    return render(request,'thirdyear/show.html',{'all_data':all_data})

def studentData(request,pk):
    all_data =Attend.objects.filter(rollno=pk)
    return render(request,'thirdyear/studentData.html',{'all_data':all_data})


def attend(request):
    all_data = Student.objects.all()
    atn_data = Attend.objects.all()
    dates = []
    for atn_date in atn_data:
        # print(atn_date.date)
        dates.append(atn_date.date)
    # print(dates,"##############")
    rollnums = []
    for data in all_data:
        rollnums.append(data.rollno)
    # print(rollnums)
    date = ''
    keys = []
    for key in request.GET:
        keys.append(key)
        date = request.GET['date']
    # print(keys,"###################3")
    for rollnum in rollnums:
        if str(rollnum) in keys:
            if str(date) in dates:
                messages.error(request,'date already exists...')
                break
            Attend.objects.create(date=str(date),rollno=rollnum, status=True)
            # print(date,rollnum,'true')
        else:
            if str(date) in dates:
                messages.error(request,'date already exists or date should not be empty')
                break
            Attend.objects.create(date=str(date),rollno=rollnum,status=False)
            # print(date,rollnum,'false',type(date),type(rollnum))
    return render(request,'thirdyear/attend.html',{'all_data':all_data})



def attendResult(request):
    all_data = Attend.objects.all()
    delete = Attend.objects.filter(date = '')
    delete.delete()

    result=[]
    for data in all_data:
        # print(data.date)
        for i in request.GET:
            # print(request.GET[i],"###################")
            if data.date == request.GET[i]:
                result .append(data)
                # print(result)

    return render(request,'thirdyear/attendResult.html',{'all_data':all_data,'result':result})


def searchResult(request):
    date = request.GET['date']
    all_data = Attend.objects.filter(date=date)


    return render(request,'thirdyear/searchResult.html',{'all_data':all_data})


def delete(request,pk):
    all_data = Attend.objects.filter(id=pk)
    all_data.delete()
    return redirect('/thirdyear/attendResult/')


def deleteStudent(request,pk):
    all_data = Student.objects.filter(rollno=pk)
    all_data.delete()
    return redirect('/thirdyear/show/')


def update(request,pk):
    all_data = Attend.objects.all()
    al_data = Attend.objects.filter(id=pk)
    for data in al_data:
        if data.status == True:
            data.status = False
            data.save()
            # print(data.status)
            return redirect('/thirdyear/attendResult/')

        else:
            data.status = True
            data.save()
            # print(data.status)
            return redirect('/thirdyear/attendResult/')
    # return render(request,'thirdyear/attendResult.html',{'all_data':all_data})




def logout(request):
    auth.logout(request)
    return redirect('/')