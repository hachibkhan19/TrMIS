from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('course.urls')),
    path('batch/', include('batch.urls')),
    path('course-detail/', include('training.urls')),
    path('trainee-attendance/', include('trainee_attendance.urls')),
   
]
