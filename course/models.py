from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class CourseCategory(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'
        db_table = 'course_category_type'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        db_table = 'course_type'

    def __str__(self):
        return self.name

class CourseMaterial(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    file_url = models.FileField()

    class Meta:
        verbose_name = 'Course Material'
        verbose_name_plural = 'Course Materials'
        db_table = 'course_material'

        