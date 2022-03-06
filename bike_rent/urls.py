"""bike_rent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from system.views import admin_bike_list,bike_created,msg_delete,admin_msg,order_list , order_update,order_delete
from accounts.views import (login_view, register_view, logout_view)
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import  re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_bike_list, name='adminIndex'),
    path('bike/', include('system.urls')),
    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('create/', bike_created, name = "bike_create"),
    path('message/', admin_msg, name='message'),


    path('listOrder/', order_list, name = "order_list"),

    path('<int:id>/editOrder/', order_update, name = "order_edit"),
    path('<int:id>/deleteOrder/', order_delete, name = "order_delete"),

    path('<int:id>/deletemsg/', msg_delete, name = "msg_delete"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
