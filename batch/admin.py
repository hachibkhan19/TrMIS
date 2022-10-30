from django.contrib import admin
from .models import Batch

# Register your models here.
class BatchAdmin(admin.ModelAdmin):
    list_display= [f.name for f in Batch._meta.fields]

admin.site.register(Batch, BatchAdmin)