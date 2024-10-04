from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from .forms import CourseForm
from .models import Teacher, Student, Course


class IndexView(TemplateView):
    template_name = "learning/index.html"

class TeachersListView(ListView):
    model = Teacher
    template_name = 'learning/teachers_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'learning/teacher_detail.html'
    context_object_name = 'teacher'

class StudentListView(ListView):
    model = Student
    template_name = 'learning/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'learning/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'learning/student_create.html'


class CourseCreateView(CreateView):
    template_name = "learning/course-create.html"
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("learning:teachers_list")

