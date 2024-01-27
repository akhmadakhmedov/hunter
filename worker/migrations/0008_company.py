# Generated by Django 5.0.1 on 2024-01-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0007_resume_created_at_resume_text_resume_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('worker', models.ManyToManyField(blank=True, null=True, to='worker.worker')),
            ],
        ),
    ]
