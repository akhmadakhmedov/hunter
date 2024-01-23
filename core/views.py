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

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  #1 id
    candidates = vacancy_object.candidates.all()  #list
    context = {'vacancy': vacancy_object,
               "candidates_list": candidates}
    return render(request, 'vacancy_page.html', context)

def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)

def candidates(request):
    return render(request, 'candidates.html')

def search(request):
    word = request.GET['keyword']
    vacancy_list = Vacancy.objects.filter(title__contains = word)
    context = {'vacancies': vacancy_list}
    return render(request, 'vacancies.html', context)


