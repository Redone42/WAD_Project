from django.contrib import admin
from .models import Student,Lecturer,Mentor,Note,Course,MentoringSession
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Mentor)
admin.site.register(Note)
admin.site.register(MentoringSession)