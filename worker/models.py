from django.db import models
from django.contrib.auth.models import User

class Worker(models.Model):
    user = models.OneToOneField(
        to = User,
        null=True,
        blank=False,
        on_delete=models.CASCADE

    )
    name = models.CharField(max_length=55)
    specialisation = models.CharField(max_length=55)
    expected_salary = models.IntegerField()
    is_searching = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        to = Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author.username

class Resume(models.Model):
    worker = models.ForeignKey(
        to = Worker,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    age = models.IntegerField()
    experience_year = models.IntegerField()

    def __str__(self):
        return self.name