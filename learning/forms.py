from django import forms
from .models import Course, Student, Teacher
from django.utils.translation import gettext_lazy as _
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "course_name",
            "description",
            "peirod_month",
            "course_for",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"cols": 40, "rows": 5}),
        }
        labels = {
            "course_name": _("Название курса :"),
            "description": _("Описание курса :"),
            "peirod_month": _("Период обучения :"),
            "course_for": _("Курс для тех :")
        }
        help_texts = {
            "description": _("Описание курса"),
        }
        error_messages = {
            "course_name": {
                "max_length": _("Название курса слишком длинное"),
            },
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_name",
            "email",
            "birth_date",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "teacher_name",
            "about_self",
            "email",
            "birth_date",
        ]
        widgets = {
            # "teacher_name": forms.Textarea(attrs={"cols": 40, "rows": 5}),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "teacher_name": _("Имя учителя :"),
            "about_self": _("Немного об учителе :"),
            "email": _("Email :"),
            "birth_date": _("Дата рождения :"),
        }
