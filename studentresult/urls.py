"""
URL configuration for studentresult project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from studentresult_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='127.0.0.1:8000/admin/'),
# ------------------------------------------------------------------------------
    path('', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('ssc', views.ssc, name='ssc'),
    path('inter_1y', views.inter_1y, name='inter_1y'),
    path('inter_2y', views.inter_2y, name='inter_2y'),
    path('degree_1y', views.degree_1y, name='degree_1y'),
    path('degree_2y', views.degree_2y, name='degree_2y'),
    path('degree_3y', views.degree_3y, name='degree_3y'),
    path('btech_1y', views.btech_1y, name='btech_1y'),
    path('btech_2y', views.btech_2y, name='btech_2y'),
    path('btech_3y', views.btech_3y, name='btech_3y'),
    path('btech_4y', views.btech_4y, name='btech_4y'),
#-------------------------------------------------------------------------------













]
