from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.batch, name='batch_url'),
    path('api/', api.BatchApiView.as_view(), name='batch_url')

]