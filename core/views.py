from django.shortcuts import HttpResponse, render
from .models import Vacancy, Company

def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return HttpResponse("Here are all the contacts")

def address(request):
    return HttpResponse("""
                <div>
                    <li>Pakhta abad str 144 Osh, Kyrgyzstan</li>
                    <li>Pereulok geologcheskaya 345, Bishkek</li>
                </div>
                """)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    return render(request, 'vacancies.html', context)

def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)

def candidates(request):
    return render(request, 'candidates.html')


