# Generated by Django 5.0.1 on 2024-01-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(default='No info yet')),
                ('is_relevant', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('contacts', models.CharField(max_length=100, verbose_name='Konakty')),
            ],
        ),
    ]
