"""DWT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app1 import views

from app1.views import *

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'department',DepartmentViewSet)
router.register(r'consult',ConsultViewSet)
router.register(r'medicationstyle',MedicationStyleViewSet)
router.register(r'medicationnotice',MedicationNoticeViewSet)
router.register(r'medicationrecord',MedicationRecordViewSet)


urlpatterns = [
    path('', views.index),
    path('index/', views.index,name ='index'),
    path('register/', views.register,name='register'),
    path('department/', views.department, name='department'),
    path('consult/', views.consult, name='consult'),
    path('medicationstyle/', views.medicationstyle, name='medicationstyle'),
    path('medicationnotice/', views.medicationnotice, name='medicationnotice'),

    url(r'^api/', include(router.urls)),

]
