from django.contrib import admin
from .models import Batch

# Register your models here.
class BatchAdmin(admin.ModelAdmin):
    # list_display= [f.name for f in Batch._meta.fields]
    list_display = (
        'batch_name',
        'course_name',
        'year',
        'coordinatior',
        'training_course_detail',
        'training_center',
        'start_date',
        'end_date',
    )

admin.site.register(Batch, BatchAdmin)