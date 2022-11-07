from django.urls import path
from . import api

urlpatterns = [
    path('', api.BatchApiView.as_view()),
]