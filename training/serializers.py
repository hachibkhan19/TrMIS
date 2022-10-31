from dataclasses import fields
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
        fields = ["id", "batch_name", "trainees"]


class CourseSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    batch = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("name", "batch")
     
    def get_batch(self, obj):
        batch = Batch.objects.all()
        return BatchSerializer(batch, many=True).data
