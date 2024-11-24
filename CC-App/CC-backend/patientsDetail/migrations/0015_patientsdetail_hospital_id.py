# Generated by Django 4.2.16 on 2024-10-14 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersDetail', '0012_usersdetail_health_institution'),
        ('patientsDetail', '0014_alter_patientsimageandprediction_left_eye_prediction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsdetail',
            name='hospital_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usersDetail.healthyinstitution'),
            preserve_default=False,
        ),
    ]
