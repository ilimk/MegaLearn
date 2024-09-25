from django.urls import path
from .views import IndexView, TeachersListView, StudentListView, TeacherDetailView, StudentDetailView

app_name = 'learning'


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    # path("teachers/", TeachersView.as_view(), name='teachers'),
    path("teachers-list/", TeachersListView.as_view(), name='teachers_list'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path("students_list/", StudentListView.as_view(), name='students_list'),
    path("student_detail/<int:pk>", StudentDetailView.as_view(), name='student_detail'),
]