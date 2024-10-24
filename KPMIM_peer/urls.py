from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # Main page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),  # Login page
    path('lecturer/<str:user_id>/add_note/', views.add_note, name='add_notes'),
    path('lecturer/<str:user_id>/delete_note/', views.list_and_delete_notes, name='list_and_delete_notes'),
    path('mentor/<str:user_id>/create_session/', views.create_session, name='create_session'),
    path('mentor/<str:user_id>/edit_session/', views.edit_delete_session, name='edit_session'),
    path('mentor/<str:user_id>/delete_session/<str:ses_id>/', views.delete_session, name='delete_session'),
    path('student/<str:user_id>/', views.student_profile, name='student_profile'),  # Student profile page
    path('mentor/<str:user_id>/', views.mentor_profile, name='mentor_profile'),  # Mentor profile page
    path('lecturer/<str:user_id>/', views.lecturer_profile, name='lecturer_profile'),  # Lecturer profile page
    path('mentor/<str:user_id>/search_notes/', views.search_notes, name='search_notes'),
    path('student/<str:user_id>/search_notes/', views.search_notes_student, name='search_notes_student'),
    path('student/<str:user_id>/search_mentoring_sessions/', views.search_mentoring_session, name='search_mentoring_sessions_student'),
    path('student/<str:user_id>/enroll_session/<str:ses_id>/', views.enroll_session_student, name='enroll_session_student'),

]

