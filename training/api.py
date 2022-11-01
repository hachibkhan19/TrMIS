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


class CourseApiDetails(APIView):
    def get(self, request, id):
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(f'Course no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    # def put(self, request, id):
    #     try:
    #         article = Article.objects.get(id=id)
    #     except Article.DoesNotExist:
    #         return Response(f'Article no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, id):
    #     try:
    #         article = Article.objects.get(id=id)
    #     except Article.DoesNotExist:
    #         return Response(f'Article no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)