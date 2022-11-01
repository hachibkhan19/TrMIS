from django.urls import path
from . import api


urlpatterns = [
    path('', api.CourseApiView.as_view(), name='training_course_detail_url'),
    path('training-course-detail/<int:id>/', api.CourseApiDetails.as_view(), name='course_detail_url'),

]