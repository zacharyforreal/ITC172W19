from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resource/', views.resource, name="resource"),
    path('getmeetings/', views.getmeetings, name='getmeetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]