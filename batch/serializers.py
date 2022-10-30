from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from batch.models import Batch
from trainee.models import Trainee
from trainer.models import Trainer



class TraineeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainee
        fields = "__all__"

class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = "__all__"

class BatchSerializer(serializers.ModelSerializer):
    trainee = TraineeSerializer(many=True, read_only=True)
    trainer = TrainerSerializer(many=True, read_only=True)
    coordinatior_name = serializers.CharField(source='coordinatior.name')
    training_course_detail_name = serializers.CharField(source='training_course_detail.name')
    training_center_address = serializers.CharField(source='training_center.address')


    class Meta:
        model = Batch
        fields = ("id", "batch_name", "trainee", "trainer", "coordinatior_name", "training_course_detail_name", "training_center_address")
