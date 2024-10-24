# Generated by Django 5.1 on 2024-10-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPMIM_peer', '0003_mentor_lecturer_note_student_mentoringsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='lec_id',
        ),
        migrations.RemoveField(
            model_name='mentoringsession',
            name='men_id',
        ),
        migrations.RemoveField(
            model_name='mentoringsession',
            name='stud_id',
        ),
        migrations.RemoveField(
            model_name='note',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course_id',
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
