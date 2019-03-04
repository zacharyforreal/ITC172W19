from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('reviewapptypes/', views.reviewapptypes, name="reviewapptypes"),
    path('getgames/', views.getgames, name="getgames"),
    path('gamedetail/<int:id>', views.gamedetails, name="details"),
    path('newGame/', views.newGame, name='newgame'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]

