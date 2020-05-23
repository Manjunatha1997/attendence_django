from django.contrib import admin
from leave.models import *
# Register your models here.

class leaveAdmin(admin.ModelAdmin):
    list_display = ['rollno','start_date','end_date','reason','status']

admin.site.register(ApplyLeave,leaveAdmin)