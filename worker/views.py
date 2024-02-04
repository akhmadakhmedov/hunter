from django.shortcuts import render, redirect, HttpResponse
from .models import Worker, Resume, Company
from .forms import ResumeEditForm, AddResumeForm, CompanyForm, CompanyEditForm
from django.contrib.auth.decorators import login_required


def worker_list(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html', context)


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    vacancies = worker_object.vacancy_set.all()
    context = {'worker': worker_object,
               "vacancies": vacancies}
    return render(request, 'worker.html', context)

def resume_list(request):
    resume_list = Resume.objects.all()
    context = {"resume_list": resume_list}
    return render(request, 'resume/resume_list.html', context)


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    context = {"resume": resume_object}
    return render(request, 'resume/resume_detail.html', context)

def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker)
        return render(
            request, 'resume/resume_list.html',
            {"resumes": resume_query}
        )
    else:
        return redirect('home')

@login_required(login_url='sign-in')
def add_resume(request):
    if request.method == 'GET':
        return render(request, 'resume/resume_add.html')
    elif request.method == 'POST':
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST["form-title"]
        new_resume.text = request.POST["form-text"]
        new_resume.save()
        return HttpResponse('New resume added')

@login_required(login_url='sign-in')
def add_resume_df(request):
    if request.method == "GET":
        resume_form = AddResumeForm()
        return render(request, 'resume/resume_add_df.html', {"resume_form": resume_form})
    elif request.method == "POST":
        #adding new resume details from the user
        resume_form = AddResumeForm(request.POST)
        if resume_form.is_valid():
            new_resume = resume_form.save()
            return redirect(f'/resume-info/{new_resume.id}/')


def edit_resume(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == 'POST':
        resume.title = request.POST['edit-title']
        resume.text = request.POST['edit-text']
        resume.save()
        return redirect(f'/resume-info/{resume.id}')
    return render(
        request, 'resume/edit_resume.html', {'resume': resume}
    )


def edit_resume_df(request, id):
    resume_object = Resume.objects.get(id=id)
    if request.method == "GET":
        form = ResumeEditForm(instance=resume_object)
        return render(request, "resume/edit_resume_df.html", {"form": form})

    elif request.method == "POST":
        form = ResumeEditForm(data = request.POST, instance=resume_object, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(resume_info, id=obj.id )
        return HttpResponse("Not VALID CREDENTIALS")


def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'company/company.html', context)

def add_company(request):
    if request.method == "POST":
        #adding new compay info
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return HttpResponse("SAVEEDDD")

    company_form = CompanyForm()
    return render(request,
                      'company/add_company.html',
                      {"company_form": company_form})


def company_detail(request, id):
    company_object = Company.objects.get(id=id)  # 1 id
    #workers = company_object.candidates.all()  # list
    #context = {'company_object': company_object,
               #"candidates_list": candidates}
    return render(request, 'company/company_detail.html', {"company_object": company_object})

def company_edit(request, id):
    company_object = Company.objects.get(id=id)
    if request.method == "GET":
        form = CompanyEditForm(instance=company_object)
        return render(request, 'company/company_edit.html', {"form": form})
    elif request.method == "POST":
        form = CompanyEditForm(data=request.POST, instance=company_object)
        if form.is_valid():
            obj = form.save()
            return redirect(company_detail, id=obj.id)
        return HttpResponse("Not good")

