from django.db import models
from django.contrib.auth.models import User


class Recruiter(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name = 'recruit'
    )
    city = models.CharField(max_length=55, null=True, blank=True)
    country = models.CharField(max_length=55, null=True, blank=True)
    payment_for_fund = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.user.username
