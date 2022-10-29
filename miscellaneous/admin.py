from django.contrib import admin
from .models import Organization, Designation, Grade, Gallery, Notice

# Register your models here.
admin.site.register(Organization)
admin.site.register(Designation)
admin.site.register(Grade)
admin.site.register(Gallery)
admin.site.register(Notice)

