"""big_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from manager import views
import employee
urlpatterns = [
    path('admin/', admin.site.urls),
    path('zhu_ce/', views.zhu_ce),
    path('register/', views.register),
    path('login/', views.login),
    path('login_confirm/', views.login_confirm),
    path('employee/', include('employee.url')),



]
