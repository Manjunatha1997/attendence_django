from django.contrib import admin
from secondyear.models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','phno']

admin.site.register(Student,StudentAdmin)

class AttendAdmin(admin.ModelAdmin):
    list_display = ['rollno','status','date']

admin.site.register(Attend,AttendAdmin)
