from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from course.models import Course

class CourseSerializer(serializers.Serializer):

    class Meta:
        model = Course
        fields = '__all__'