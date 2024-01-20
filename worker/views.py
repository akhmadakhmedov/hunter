from django.shortcuts import render
from .models import Worker


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