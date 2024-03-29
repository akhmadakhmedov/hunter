from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'email', 'contacts', 'work_type']

class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'email', 'contacts', 'work_type']

