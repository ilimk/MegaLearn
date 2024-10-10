from django.db import models
import datetime

from django.urls import reverse


class Course(models.Model):
    course_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)
    peirod_month = models.IntegerField(blank=True, null=True)
    course_for = models.TextField(blank=True, null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
       return reverse('learning:course_detail', kwargs={"pk": self.pk})

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255)
    about_self = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, verbose_name='Teacher Email Address')
    birth_date = models.DateField(datetime.date(2024, 1, 1))
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.teacher_name

    def get_absolute_url(self):
       return reverse('learning:teacher_detail', kwargs={"pk": self.pk})

class Student(models.Model):
    student_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, unique=True, verbose_name='Student Email Address')
    birth_date = models.DateField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
       return reverse('learning:teacher_detail', kwargs={"pk": self.pk})

class TeacherCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.datetime.today(), blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course}, {self.teacher}'


class Group(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)
    start_date = models.DateField(default=datetime.datetime.today(), blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    archived = models.BooleanField(default=False)
