# Generated by Django 4.2.16 on 2024-10-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersDetail', '0013_alter_healthyinstitution_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthyinstitution',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]