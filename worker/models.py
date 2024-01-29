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
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    title = models.CharField(max_length=55)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(
        null=True, blank=True,
        upload_to="profile_photo/",
        verbose_name="Staffs photo"
    )


    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    ceo = models.CharField(max_length=55)
    created_date = models.DateTimeField(auto_now_add=True)
    worker = models.ManyToManyField(
        to = Worker,
        blank=True,
        related_name='company'
    )

    def __str__(self):
        return self.name

