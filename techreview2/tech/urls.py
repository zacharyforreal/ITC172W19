from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('techtypes/', views.techtypes, name="techtypes"),
    path('getproducts/', views.getproducts, name="getproducts"),
    path('productdetail/<int:id>', views.productdetails, name="details"),
    path('newProduct/', views.newProduct, name='newproduct'),
]

