from django.db import models
from worker.models import Worker

# Create your models here.
class Vacancy(models.Model):
    FULLTIME = 'FT'
    PARTTIME = 'PT'
    PROJECT_BASED = 'PB'
    WORK_TYPE = [
        (FULLTIME , "Fulltime"),
        (PARTTIME , "Parttime"),
        (PROJECT_BASED , "Project_based")
    ]
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='No info yet')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    contacts = models.CharField(max_length=100, verbose_name='Konakty')
    candidates = models.ManyToManyField(
        to = Worker,
        blank=True
    )
    category = models.ForeignKey(
        to = 'Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='kategoriya'
    )
    experience = models.IntegerField(null=True, blank=True, default=0)
    work_type = models.CharField(max_length=55, choices=WORK_TYPE, default=FULLTIME)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiii'
        ordering = ['salary']
        unique_together = [['title', 'email']]


class Skills(models.Model):
    pass



class Company(models.Model):
    name = models.CharField(max_length=55)
    address = models.TextField(default='Not mentioned')
    quantity = models.IntegerField()
    is_hunting = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(null=True, max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

