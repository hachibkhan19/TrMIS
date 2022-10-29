from pickletools import read_long1
from tabnanny import verbose
from django.db import models
from course.models import Course
from miscellaneous.models import Organization
from info.models import Location

# Create your models here.
class LocationBasedTrainingAssesment(models.Model):
    training_location = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    remarks = models.FileField()

    class Meta:
        verbose_name = 'Location Based Training Assesment'
        verbose_name_plural = 'Location Based Training Assesments'
        db_table = 'location_based_training_assesment'

class TrainingCourseDetail(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_rel')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Training Course Detail'
        verbose_name_plural = 'Training Course Details'
        db_table = 'training_course_detail'


class TrainingCenter(models.Model):
    address = models.CharField(max_length=200)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Training Center'
        verbose_name_plural = 'Training Centers'
        db_table = 'training_center'


    def __str__(self):
        return self.address