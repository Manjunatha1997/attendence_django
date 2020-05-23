
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mca/',include('mca.urls')),
    path('',include('registration.urls')),
    path('student/',include('student.urls')),
    path('leave/',include('leave.urls')),
    path('firstyear/',include('firstyear.urls')),
    path('secondyear/',include('secondyear.urls')),
    path('thirdyear/',include('thirdyear.urls')),

]
