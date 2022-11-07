from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.batch, name='batch_url'),
    path('batch-details/', api.BatchApiView.as_view(), name='batch_url'),
    # path('batch-details/<int:id>', api.BatchDetailsApiView.as_view(), name='batch_details_url')

]