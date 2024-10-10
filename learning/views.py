from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import CourseForm, StudentForm, TeacherForm
from .models import Teacher, Student, Course


class IndexView(TemplateView):
    template_name = "learning/index.html"

class TeachersListView(ListView):
    # model = Teacher
    queryset = Teacher.objects.filter(archived=False).all()
    template_name = 'learning/teachers/teachers_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'learning/teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'learning/teachers/teacher_create.html'
    form_class = TeacherForm

    # def get_success_url(self):
    #     return reverse('learning:teacher_detail', kwargs={'pk': self.object.pk})

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'learning/teachers/teacher_confirm_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('learning:teachers_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'learning/teachers/teacher_update.html'
    form_class = TeacherForm


class StudentListView(ListView):
    model = Student
    template_name = 'learning/students/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'learning/students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    template_name = 'learning/students/student_create.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('learning:student_detail')

    def get_success_url(self):
        return reverse('learning:student_detail', kwargs={'pk': self.object.pk})


class CourseListView(ListView):
    model = Course
    template_name = 'learning/courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'learning/courses/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    template_name = "learning/courses/course-create.html"
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse('learning:student_detail', kwargs={'pk': self.object.pk})