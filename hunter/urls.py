"""
URL configuration for hunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core.views import *
from worker.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('address/', address, name='address'),
    path('vacancies/', vacancy_list, name='vacancies'),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-info'),
    path('address/', address, name='address'),
    path('companies/', company_list, name='companies'),
    path('workers/', worker_list, name='workers'),
    path('worker/<int:id>/', worker_info, name='worker_info'),
    path('resume-list/', resume_list, name='resume_list'),
    path('resume-info/<int:id>/', resume_info, name='resume_info'),
    path('my-resume/', my_resume, name='my-resume'),
    path('add-resume/', add_resume, name='add-resume'),
    path('search/', search, name='search'),

]
