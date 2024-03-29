"""proytectocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from tasks import views
from tasks.views import guardar_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('singup/', views.singup, name = 'singup'),
    path('task/', views.task, name = 'task'),
    path('logout/', views.singout, name = 'logout'),
    path('singin/', views.singin, name = 'singin'),
    path('task/create/', views.create_task, name = 'create_task'),
    path('calc/', views.calc, name = 'calc'),
    path('program/', views.program, name = 'program'),
    path('exercises/', views.exercises, name = 'exercises'),
    path('practic/', views.practic, name = 'practic'),
    path('guardar_video/', guardar_video, name='guardar_video'),
]
