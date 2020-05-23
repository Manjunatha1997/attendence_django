from django.urls import path
from leave.views import *
urlpatterns = [
    path('applyLeave/',applyLeave),
    path('leaveStatus/<int:pk>/',leaveStatus),
    path('checkLeaveApplied/', checkLeaveApplied),
    path('approved/<int:pk>/', approved),
    path('canceled/<int:pk>/', canceled),

]