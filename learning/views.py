from django.views.generic import TemplateView, ListView, DetailView, CreateView

from learning.models import Teacher, Student


class IndexView(TemplateView):
    template_name = "learning/index.html"


# class TeachersView(TemplateView):
#     template_name = 'learning/teachers_list.html'
#
#     extra_context = {
#         'pi':3.1415,
#     }
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(
#             teachers=Teacher.objects.all(),
#         )
#         return context

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