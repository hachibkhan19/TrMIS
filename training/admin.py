from django.contrib import admin
from .models import LocationBasedTrainingAssesment, TrainingCourseDetail, TrainingCenter

# Register your models here.
admin.site.register(LocationBasedTrainingAssesment)
admin.site.register(TrainingCourseDetail)
admin.site.register(TrainingCenter)
