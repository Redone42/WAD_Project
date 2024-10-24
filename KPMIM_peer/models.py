from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=100)

class Student(models.Model):
    stud_id = models.CharField(max_length=50,primary_key=True)
    stud_name = models.CharField(max_length=100)
    stud_email = models.EmailField(unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_username = models.CharField(max_length=50)
    stud_pass = models.CharField(max_length=50)

class Lecturer(models.Model):
    lec_id = models.CharField(max_length=50,primary_key=True)
    lec_name = models.CharField(max_length=100)
    lec_email = models.EmailField(unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    lec_username = models.CharField(max_length=50)
    lec_pass = models.CharField(max_length=50)

class Mentor(models.Model):
    men_id = models.CharField(max_length=50,primary_key=True)
    men_name = models.CharField(max_length=100)
    men_email = models.EmailField(unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    men_username = models.CharField(max_length=50)
    men_pass = models.CharField(max_length=50)

class Note(models.Model):
    note_id = models.CharField(max_length=50,primary_key=True)
    lec_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=100)
    note_link = models.CharField(max_length=300)

class MentoringSession(models.Model):
    ses_id = models.CharField(max_length=50,primary_key=True)
    ses_name = models.CharField(max_length=50)
    men_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, blank=True)
    ses_date = models.DateField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)