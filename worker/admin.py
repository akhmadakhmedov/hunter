from django.contrib import admin
from .models import Worker, Comment, Resume, Company


admin.site.register(Worker)
admin.site.register(Comment)
admin.site.register(Resume)
admin.site.register(Company)