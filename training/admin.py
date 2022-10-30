from django.contrib import admin
from .models import LocationBasedTrainingAssesment, TrainingCourseDetail, TrainingCenter


class TraininCourseDetailAdmin(admin.ModelAdmin):
        list_display= [f.name for f in TrainingCourseDetail._meta.fields]


# Register your models here.
admin.site.register(LocationBasedTrainingAssesment)
admin.site.register(TrainingCourseDetail,TraininCourseDetailAdmin)
admin.site.register(TrainingCenter)
