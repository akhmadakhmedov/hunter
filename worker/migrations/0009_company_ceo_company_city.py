# Generated by Django 5.0.1 on 2024-01-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0008_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='CEO',
            field=models.CharField(default='sasa', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='ddd', max_length=55),
            preserve_default=False,
        ),
    ]
