from django.contrib import admin
from .models import User, Address, Contact, Location
# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Location)
