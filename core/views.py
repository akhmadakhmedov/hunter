from django.shortcuts import HttpResponse, render, redirect
from .models import Vacancy, Company
from django.contrib.auth.models import User
from .forms import VacancyForm, VacancyEditForm

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
    return render(request, 'vacancy/vacancies.html', context)

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  #1 id
    candidates = vacancy_object.candidates.all()  #list
    context = {'vacancy': vacancy_object,
               "candidates_list": candidates}
    return render(request, 'vacancy/vacancy_page.html', context)


def add_vacancy(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title = request.POST["title"],
            salary = int(request.POST["salary"]),
            description = request.POST["description"],
            email = request.POST["email"],
            contacts = request.POST["contacts"]
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_add.html')


def add_vacancy_df(request):
    if request.method == "POST":
        #adding new info's from the user
        vacancy_form = VacancyForm(request.POST)
        if vacancy_form.is_valid():
            new_vacancy = vacancy_form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(request,
                  'vacancy/vacancy_add_df.html',
                  {"vacancy_form": vacancy_form})


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contact = request.POST["contact"]
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(request, 'vacancy/vacancy_edit_form.html', {"vacancy": vacancy})

def vacancy_edit_df(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    if request.method == "GET":
        form = VacancyEditForm(instance=vacancy_object)
        return render(request, 'vacancy/vacancy_edit_df.html', {"form": form})
    elif request.method == "POST":
        form = VacancyEditForm(data = request.POST, instance=vacancy_object)
        if form.is_valid():
            obj = form.save()
            return redirect(vacancy_detail, id=obj.id)
        return HttpResponse("Not good")


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



def reg_view(request):
    if request.method == "POST":
        user = User(
            username = request.POST['username']
        )
        user.save()
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponse('ready')



    return render(request, 'auth/registr.html')
