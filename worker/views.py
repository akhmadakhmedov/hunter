from django.shortcuts import render, redirect, HttpResponse
from .models import Worker, Resume


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
    return render(request, 'resume_list.html', context)


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    context = {"resume": resume_object}
    return render(request, 'resume_detail.html', context)

def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker)
        return render(
            request, 'resume_list.html',
            {"resumes": resume_query}
        )
    else:
        return redirect('home')

def add_resume(request):
    if request.method == 'GET':
        return render(request, 'resume_add.html')
    elif request.method == 'POST':
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST["form-title"]
        new_resume.text = request.POST["form-text"]
        new_resume.save()
        return HttpResponse('New resume added')


def edit_resume(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == 'POST':
        resume.title = request.POST['edit-title']
        resume.text = request.POST['edit-text']
        resume.save()
        return redirect(f'/resume-info/{resume.id}')
    return render(
        request, 'edit_resume.html', {'resume': resume}
    )




