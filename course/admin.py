from django.contrib import admin
from .models import CourseCategory, Course, CourseMaterial

# Register your models here.
admin.site.register(CourseCategory)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseMaterial)
