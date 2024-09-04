from django.db import models
import datetime


class Course(models.Model):
    course_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True, verbose_name='Teacher Email Address')
    birth_date = models.DateField()

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, unique=True, verbose_name='Student Email Address')
    birth_date = models.DateField(blank=True)

    def __str__(self):
        return self.student_name


class TeacherCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.datetime.today(), blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.course}, {self.teacher}'


class Group(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)
    start_date = models.DateTimeField(default=datetime.datetime.today(), blank=False, null=False)
    end_date = models.DateTimeField(blank=True, null=True)
