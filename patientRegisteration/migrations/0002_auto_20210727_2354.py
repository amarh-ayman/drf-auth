# Generated by Django 3.2.5 on 2021-07-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientRegisteration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientregister',
            name='IdNum',
        ),
        migrations.AddField(
            model_name='patientregister',
            name='idNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patientregister',
            name='age',
            field=models.IntegerField(),
        ),
    ]