# Generated by Django 5.0.1 on 2024-01-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_company'),
        ('worker', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='candidates',
            field=models.ManyToManyField(blank=True, to='worker.worker'),
        ),
    ]
