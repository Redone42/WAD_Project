# Generated by Django 5.1 on 2024-10-15 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPMIM_peer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='lecturer',
        ),
        migrations.RemoveField(
            model_name='mentoringsession',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='mentoringsession',
            name='student',
        ),
        migrations.RemoveField(
            model_name='note',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='MentoringSession',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
