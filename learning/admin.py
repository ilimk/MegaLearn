from django.contrib import admin

from .models import Course, Teacher, Student, TeacherCourse, Group


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "pk", "course_name"
    list_display_links = "pk", "course_name"


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "pk", "teacher_name", "email"
    list_display_links = "pk", "teacher_name", "email"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "pk", "student_name", "email", "birth_date"
    list_display_links = "pk", "student_name"


@admin.register(TeacherCourse)
class TeacherCoursesAdmin(admin.ModelAdmin):
    list_display = "pk", "course", "teacher", "start_date", "end_date"
    list_display_links = "pk", "course", "teacher"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "teacher_list", "start_date", "end_date"
    list_display_links = "pk", "name"
    # list_filter = "teachers"

    def teacher_list(self, obj: Group) -> str:
        teachers = obj.teachers.all()
        return ", ".join(c.teacher_name for c in teachers)
