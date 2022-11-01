from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import TrainingCourseDetail
from course.models import Course
from batch.models import Batch
from trainer.models import Trainer

class BatchSerializer(serializers.ModelSerializer):
    trainees = serializers.IntegerField(source="trainee.count", read_only=True)

    class Meta:
        model = Batch
        fields = ["id", "batch_name", "trainees", "year"]


class CourseSerializer(serializers.ModelSerializer):
    batch = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "name", "batch")
     
    def get_batch(self, name):
        batch = Batch.objects.filter(training_course_detail__course__name=name)
        return BatchSerializer(batch, many=True).data
