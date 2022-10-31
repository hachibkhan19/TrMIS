from django.urls import path
from . import api


urlpatterns = [
    path('', api.CourseApiView.as_view(), name='training_course_detail_url'),

]