"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from todoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser'),

    #todo
    path('',views.home,name='home'),
    path('create/',views.createtodo,name='createtodo'),
    path('current/',views.currenttodo,name='currenttodo'),
    path('completed/',views.completedtodo,name='completedtodo'),
    path('todoApp/<int:todo_id>/',views.viewtodo,name='viewtodo'),
    path('todoApp/<int:todo_id>/complete/',views.completetodo,name='completetodo'),
    path('todoApp/<int:todo_id>/delete/',views.deletetodo,name='deletetodo'),
    

    #API 
    path('api/',include('api.urls')),
]
