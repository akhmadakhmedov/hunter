from django import forms
from .models import Resume, Company

class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text']

class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"