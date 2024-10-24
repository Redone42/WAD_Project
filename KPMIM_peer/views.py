from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Mentor, Lecturer, Course, Note, MentoringSession

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        course_id = request.POST.get('course')
        user_id = request.POST.get('id')  # Retrieve the entered ID

        # Find the course based on the selected course_id
        course = Course.objects.get(course_id=course_id)

        # Save the data to the appropriate model based on the selected role
        if role == 'Student':
            Student.objects.create(
                stud_id=user_id,  # Save the entered ID
                stud_name=name,
                stud_email=email,
                stud_username=username,
                stud_pass=password,
                course_id=course
            )
        elif role == 'Mentor':
            Mentor.objects.create(
                men_id=user_id,  # Save the entered ID
                men_name=name,
                men_email=email,
                men_username=username,
                men_pass=password,
                course_id=course
            )
        elif role == 'Lecturer':
            Lecturer.objects.create(
                lec_id=user_id,  # Save the entered ID
                lec_name=name,
                lec_email=email,
                lec_username=username,
                lec_pass=password,
                course_id=course
            )

        # Redirect to the login page after successful registration
        return redirect('login')  # Update 'login' with the actual URL name for your login page

    # Render the registration form template
    return render(request, 'register.html')



def main_page(request):
    return render(request, 'index.html')  # Ensure 'index.html' matches your main page template filename



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user exists in the Student table
        try:
            student = Student.objects.get(stud_username=username, stud_pass=password)
            # Redirect to the student profile page
            return redirect('student_profile', user_id=student.stud_id)
        except Student.DoesNotExist:
            pass

        # Check if the user exists in the Mentor table
        try:
            mentor = Mentor.objects.get(men_username=username, men_pass=password)
            # Redirect to the mentor profile page
            return redirect('mentor_profile', user_id=mentor.men_id)
        except Mentor.DoesNotExist:
            pass

        # Check if the user exists in the Lecturer table
        try:
            lecturer = Lecturer.objects.get(lec_username=username, lec_pass=password)
            # Redirect to the lecturer profile page
            return redirect('lecturer_profile', user_id=lecturer.lec_id)
        except Lecturer.DoesNotExist:
            pass

        # If credentials don't match any role, show an error
        return render(request, 'login.html', {'error': 'Invalid username or password'})

    # GET request, render the login page
    return render(request, 'login.html')



def student_profile(request, user_id):
    # Fetch the student from the database by user_id
    student = Student.objects.get(stud_id=user_id)
    
    # Pass the student object to the template
    return render(request, 'student_prof.html', {'student': student})

# Mentor profile view
def mentor_profile(request, user_id):
    mentor = Mentor.objects.get(men_id=user_id)
    return render(request, 'mentor_prof.html', {'mentor': mentor})

# Lecturer profile view
def lecturer_profile(request, user_id):
    lecturer = Lecturer.objects.get(lec_id=user_id)
    return render(request, 'lecturer_prof.html', {'lecturer': lecturer})

def add_note(request, user_id):
    # Ensure the lecturer exists
    try:
        lecturer = Lecturer.objects.get(lec_id=user_id)
    except Lecturer.DoesNotExist:
        return render(request, 'add_note.html', {'error': 'Lecturer not found'})

    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        note_name = request.POST.get('note_name')
        course_id = request.POST.get('course_id')
        note_link = request.POST.get('note_link')

        # Try to create the Note object
        try:
            course = Course.objects.get(course_id=course_id)

            # Create and save the note
            Note.objects.create(
                note_id=note_id,
                lec_id=lecturer,
                course_id=course,
                note_name=note_name,
                note_link=note_link
            )

            # Redirect to the lecturer's profile page after successful creation
            return redirect('lecturer_profile', user_id=lecturer.lec_id)

        except Course.DoesNotExist:
            return render(request, 'add_note.html', {'error': 'Course not found', 'all_courses': Course.objects.all().values()})

    # GET request - Display the form
    all_courses = Course.objects.all().values()
    context = {
        'all_courses': all_courses,
    }
    return render(request, 'add_note.html', context)

def list_and_delete_notes(request, user_id):
    # Fetch the lecturer based on the user ID
    try:
        lecturer = Lecturer.objects.get(lec_id=user_id)
    except Lecturer.DoesNotExist:
        return render(request, 'delete_note.html', {'error': 'Lecturer not found'})

    # Fetch all notes created by the lecturer
    notes = Note.objects.filter(lec_id=lecturer)

    # Handle note deletion
    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        try:
            note = Note.objects.get(note_id=note_id)
            note.delete()  # Delete the note
        except Note.DoesNotExist:
            return render(request, 'delete_note.html', {'error': 'Note not found', 'notes': notes, 'lecturer': lecturer})

        # Redirect back to the same page after deletion
        return redirect('list_and_delete_notes', user_id=user_id)

    # Render the delete_note template with the list of notes
    return render(request, 'delete_note.html', {'lecturer': lecturer, 'notes': notes})

def create_session(request, user_id):
    # Ensure the mentor exists
    try:
        mentor = Mentor.objects.get(men_id=user_id)
    except Mentor.DoesNotExist:
        return render(request, 'create_session.html', {'error': 'Mentor not found'})

    if request.method == 'POST':
        ses_id = request.POST.get('ses_id')
        ses_name = request.POST.get('ses_name')
        ses_date = request.POST.get('ses_date')
        course_id = request.POST.get('course_id')

        # Ensure the course exists
        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return render(request, 'create_session.html', {
                'error': 'Course not found',
                'courses': Course.objects.all()
            })

        # Create the mentoring session
        MentoringSession.objects.create(
            ses_id=ses_id,
            ses_name=ses_name,
            ses_date=ses_date,
            course_id=course,
            men_id=mentor,
            stud_id=None  # Initially, no student is assigned; you can handle this assignment later
        )

        # Redirect to the mentor profile after successful creation
        return redirect('mentor_profile', user_id=user_id)

    # GET request - Display the form with available courses
    courses = Course.objects.all()
    context = {
        'mentor': mentor,
        'courses': courses,
    }
    return render(request, 'create_session.html', context)

def edit_delete_session(request, user_id):
    # Fetch the mentor based on the user ID
    try:
        mentor = Mentor.objects.get(men_id=user_id)
    except Mentor.DoesNotExist:
        return render(request, 'edit_delete_session.html', {'error': 'Mentor not found'})

    # Fetch all mentoring sessions for this mentor
    sessions = MentoringSession.objects.filter(men_id=mentor)

    if request.method == 'POST':
        # If it's an edit request
        ses_id = request.POST.get('ses_id')
        ses_name = request.POST.get('ses_name')
        ses_date = request.POST.get('ses_date')
        course_id = request.POST.get('course_id')

        try:
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return render(request, 'edit_delete_session.html', {
                'error': 'Course not found',
                'sessions': sessions,
                'courses': Course.objects.all(),
                'mentor': mentor
            })

        try:
            session = MentoringSession.objects.get(ses_id=ses_id, men_id=mentor)
            session.ses_name = ses_name
            session.ses_date = ses_date
            session.course_id = course
            session.save()
        except MentoringSession.DoesNotExist:
            return render(request, 'edit_delete_session.html', {
                'error': 'Session not found',
                'sessions': sessions,
                'courses': Course.objects.all(),
                'mentor': mentor
            })

        # Redirect back to the edit page after successful update
        return redirect('edit_session', user_id=user_id)

    # GET request - Display the form with sessions and courses
    courses = Course.objects.all()
    context = {
        'sessions': sessions,
        'courses': courses,
        'mentor': mentor,
    }
    return render(request, 'edit_delete_session.html', context)

def delete_session(request, user_id, ses_id):
    # Ensure the session belongs to the mentor and delete it
    try:
        session = MentoringSession.objects.get(ses_id=ses_id, men_id=user_id)
        session.delete()
        return redirect('edit_session', user_id=user_id)
    except MentoringSession.DoesNotExist:
        return redirect('edit_session', user_id=user_id)

def search_notes(request, user_id):
    mentor = Mentor.objects.get(men_id=user_id)
    notes = None

    if 'course_id' in request.GET:
        course_id = request.GET.get('course_id')
        
        try:
            course = Course.objects.get(course_id=course_id)
            # Fetch the notes based on the course_id
            notes = Note.objects.filter(course_id=course)
        except Course.DoesNotExist:
            notes = None

    return render(request, 'search_notes.html', {'mentor': mentor, 'notes': notes})


def search_notes_student(request, user_id):
    student = get_object_or_404(Student, stud_id=user_id)
    notes = None

    if 'course_id' in request.GET:
        course_id = request.GET.get('course_id')

        try:
            course = Course.objects.get(course_id=course_id)
            # Fetch the notes based on the course_id
            notes = Note.objects.filter(course_id=course)
        except Course.DoesNotExist:
            notes = None

    return render(request, 'search_notes_student.html', {'student': student, 'notes': notes})


def search_mentoring_session(request, user_id):
    student = get_object_or_404(Student, stud_id=user_id)
    sessions = None

    if 'course_id' in request.GET:
        course_id = request.GET.get('course_id')

        try:
            course = Course.objects.get(course_id=course_id)
            # Fetch the mentoring sessions based on the course_id
            sessions = MentoringSession.objects.filter(course_id=course, stud_id__isnull=True)
        except Course.DoesNotExist:
            sessions = None

    return render(request, 'search_mentoring_session.html', {'student': student, 'sessions': sessions})


def enroll_session_student(request, user_id, ses_id):
    student = get_object_or_404(Student, stud_id=user_id)
    session = get_object_or_404(MentoringSession, ses_id=ses_id)

    # Enroll the student in the mentoring session by saving their stud_id
    session.stud_id = student
    session.save()

    return redirect('student_profile', user_id=student.stud_id)
