# Generated by Django 2.2.7 on 2019-11-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level_of_study',
            field=models.CharField(choices=[('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Degree', 'Degree'), ('Master', 'Master')], max_length=15),
        ),
    ]
