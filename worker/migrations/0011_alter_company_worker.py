# Generated by Django 5.0.1 on 2024-01-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0010_rename_ceo_company_ceo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='worker',
            field=models.ManyToManyField(blank=True, null=True, related_name='company', to='worker.worker'),
        ),
    ]