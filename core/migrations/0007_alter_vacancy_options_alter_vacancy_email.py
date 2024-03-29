# Generated by Django 5.0.1 on 2024-01-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_vacancy_options_vacancy_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['salary'], 'verbose_name': 'Vakansiya', 'verbose_name_plural': 'Vakansiii'},
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
