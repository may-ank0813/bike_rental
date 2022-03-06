from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = "home"),
    path('bikelist/', views.bike_list, name = "bike_list"),
    path('<int:id>/', views.bike_detail ,name = "bike_detail"),

    path('createOrder/', views.order_created, name = "order_create"),

    path('detail/<int:id>/', views.order_detail, name = "order_detail"),
    path('<int:id>/edit/', views.bike_update, name = "bike_edit"),

    path('<int:id>/delete/', views.bike_delete, name = "bike_delete"),
    path('<int:id>/deleteOrder/', views.order_delete , name = "order_delete"),

    path('contact/', views.contact, name = "contact"),
    path('newbike/', views.newbike, name = "newbike"),
    path('<int:id>/like/',views.like_update, name = "like"),
]