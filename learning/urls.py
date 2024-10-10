from django.urls import path
from .views import (
        IndexView,
        TeachersListView,
        TeacherDetailView,
        TeacherCreateView,
        TeacherDeleteView,
        TeacherUpdateView,
        StudentListView,
        StudentDetailView,
        CourseCreateView,
        CourseDetailView,
        CourseListView,
        StudentCreateView,
)

app_name = 'learning'


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    # path("teachers/", TeachersView.as_view(), name='teachers'),
    path("teachers-list/", TeachersListView.as_view(), name='teachers_list'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/add/', TeacherCreateView.as_view(), name='teacher_add'),
    path('teacher/<int:pk>/confirm-delete/', TeacherDeleteView.as_view(), name='teacher-confirm-delete'),
    path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher-edit'),
    path("students_list/", StudentListView.as_view(), name='students_list'),
    path("student_detail/<int:pk>", StudentDetailView.as_view(), name='student_detail'),
    path("student/add/", StudentCreateView.as_view(), name='student_add'),
    path("course-list/", CourseListView.as_view(), name='course_list'),
    path("course_detail/<int:pk>", CourseDetailView.as_view(), name='course_detail'),
    path('course/add/', CourseCreateView.as_view(), name='course-create'),
]