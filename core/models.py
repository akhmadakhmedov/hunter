from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='No info yet')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Konakty')


    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=55)
    address = models.TextField(default='Not mentioned')
    quantity = models.IntegerField()
    is_hunting = models.BooleanField(default=True)

    def __str__(self):
        return self.name

