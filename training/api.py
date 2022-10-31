from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TrainingCourseDetail
from rest_framework import status
from batch.models import Batch
from course.models import Course
from .serializers import CourseSerializer
from rest_framework import generics

class CourseApiView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
