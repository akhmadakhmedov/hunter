from django.shortcuts import HttpResponse, render
from .models import Vacancy


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About us info's")


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

