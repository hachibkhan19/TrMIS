from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse

from .models import Course
from training.models import TrainingCourseDetail
from batch.models import Batch

# Create your views here.
def course(request):
    # course = Course.objects.select_related()
    # training_course_detail = TrainingCourseDetail.objects.select_related()
    # batch = Batch.objects.select_related()


    # context = {
    #     "courses":course,
    #     'training_course_details': training_course_detail,
    #     'batches': batch
    # }
    # course_name = Course.objects.filter(name='CSE-132')
    # batch = TrainingCourseDetail.objects.filter(course__name='CSE-132')

    batch = Batch.objects.filter(training_course_detail__course__name='Arts')
    course = Course.objects.filter(course_rel__name='Lab')
    print(course)

    context = {
        "batches": batch
    }

    return render(request, 'index.html', context)
