from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recruiter
from .forms import RecruiterEditForm, RecruiterUpdateForm
from django.urls import reverse_lazy

class RecruitView(View):
    def get(self, request):
        recruiters = Recruiter.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})

class RecruitListView(LoginRequiredMixin, ListView):
    model = Recruiter

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = "__all__"

class RecruiterGenericUpdateView(UpdateView):
    model = Recruiter
    fields = [f.name for f in Recruiter._meta.get_fields() if f.name not in ['id', 'user']]
    template_name = 'recruit/generic_update.html'
    success_url = reverse_lazy('recruiter-list-class')

class RecruiterUpdateView(View):
    template = 'recruit/update.html'

    def get_context(self, *args):
        id = kwargs['id']
        recruiter_object = Recruiter.objects.get(id=id)
        form = RecruiterUpdateForm(instance=recruiter_object)
        context = {}
        context["form"] = form
        context["recruiter"] = recruiter_object
        return context

    def my_render(self, request, context):
        return render(request,
                      self.template,
                      {"form": form})


    def get(self, request, *args, **kwargs):
        context = self.get_context(**kwargs)
        return self.my_render(request, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(**kwargs)
        context['form'] = RecruiterUpdateForm(instance=context['recruiter'], data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Info edited')
        else:
            messages.add_message(request, messages.INFO, 'Wrong credentials')
        return self.my_render(request, context)


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'recruit/list.html', {"recruiters": recruiters})

def recruiter_detail(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    return render(request, 'recruit/detail.html', {"recruiter_object": recruiter_object})

def recruiter_edit(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    if request.method == "GET":
        form = RecruiterEditForm(instance=recruiter_object)
        return render(request, 'recruit/recruit_edit.html', {"form": form})
    elif request.method == "POST":
        form = RecruiterEditForm(data=request.POST, instance=recruiter_object)
        if form.is_valid():
            obj = form.save()
            return redirect(recruiter_detail, pk=obj.pk)
        return HttpResponse("Not good")
