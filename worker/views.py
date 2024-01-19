from django.shortcuts import render
from .models import Worker


def worker_list(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html', context)
