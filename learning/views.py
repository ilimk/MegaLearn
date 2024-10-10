from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db import IntegrityError
from .forms import CourseForm, StudentForm, TeacherForm
from .models import Teacher, Student, Course
# from django.utils.translation import gettext_lazy as _


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

    # def form_valid(self, form):
    #     try:
    #         return super().form_valid(form)
    #     except IntegrityError:
    #         form.add_error('birth_date', 'Пожалуйста, укажите дату. Это полевьваылоатлыо не может быть пустым.')
    #         return self.form_invalid(form)
    #
    # def form_invalid(self, form):
    #     # Можно добавить дополнительную логику, если необходимо
    #     return super().form_invalid(form)


class StudentListView(ListView):
    queryset = Student.objects.filter(archived=False).all()
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

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'learning/students/student_confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('learning:students_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'learning/students/student_update.html'
    form_class = StudentForm

    # def form_valid(self, form):
    #     try:
    #         return super().form_valid(form)
    #     except IntegrityError:
    #         form.add_error('birth_date', 'Пожалуйста, укажите дату. Это полевьваылоатлыо не может быть пустым.')
    #         return self.form_invalid(form)
    #
    # def form_invalid(self, form):
    #     # Можно добавить дополнительную логику, если необходимо
    #     return super().form_invalid(form)


class CourseListView(ListView):
    queryset = Course.objects.filter(archived=False).all()
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


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'learning/courses/course_confirm_delete.html'
    context_object_name = 'course'
    success_url = reverse_lazy('learning:course_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'learning/courses/course_update.html'
    form_class = CourseForm