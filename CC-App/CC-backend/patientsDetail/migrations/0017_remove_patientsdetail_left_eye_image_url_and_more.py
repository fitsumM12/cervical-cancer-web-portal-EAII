# Generated by Django 4.2.16 on 2024-10-21 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientsDetail', '0016_rename_hospital_id_patientsdetail_health_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientsdetail',
            name='left_eye_image_url',
        ),
        migrations.RemoveField(
            model_name='patientsdetail',
            name='left_eye_prediction',
        ),
        migrations.RemoveField(
            model_name='patientsdetail',
            name='right_eye_image_url',
        ),
        migrations.RemoveField(
            model_name='patientsdetail',
            name='right_eye_prediction',
        ),
    ]
