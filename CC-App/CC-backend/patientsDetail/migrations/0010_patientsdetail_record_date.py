# Generated by Django 4.2.16 on 2024-10-05 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patientsDetail', '0009_delete_hospitalsdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsdetail',
            name='record_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]