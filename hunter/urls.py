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
from django.urls import path, include
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('address/', address, name='address'),

    path('vacancies/', vacancy_list, name='vacancies'),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-info'),
    path('add-vacancy/', add_vacancy, name='add-vacancy'),
    path('add-vacancy-df/', add_vacancy_df, name='add-vacancy-df'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('vacancy-edit-df/<int:id>/', vacancy_edit_df, name='vacancy-edit-df'),

    path('address/', address, name='address'),

    path('companies/', company_list, name='companies'),
    path('company-list/', company_list, name='companies'),
    path('company/<int:id>', company_detail, name='company-info'),
    path('add-company', add_company, name='add-company'),
    path('company-edit/<int:id>', company_edit, name='company-edit'),

    path('workers/', worker_list, name='workers'),
    path('worker/<int:id>/', worker_info, name='worker_info'),

    path('resume-list/', resume_list, name='resume_list'),
    path('resume-info/<int:id>/', resume_info, name='resume_info'),
    path('my-resume/', my_resume, name='my-resume'),
    path('add-resume/', add_resume, name='add-resume'),
    path('add-resume-df/', add_resume_df, name='add-resume-df'),
    path('edit-resume/<int:id>/', edit_resume, name='edit-resume'),
    path('edit-resume_df/<int:id>/', edit_resume_df, name='edit-resume-df'),


    path('search/', search, name='search'),
    path('registration/', reg_view, name='reg'),
    path('sign-in/', sign_in, name='sign-in'),
    path('login-generic/', LoginView.as_view(), name='login-generic'),
    path('recruit/', include('recruit.urls')),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
