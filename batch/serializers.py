from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from batch.models import Batch
from trainee.models import Trainee
from trainer.models import Trainer
from django.utils.timezone import now




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
    course_name = serializers.CharField(source="training_course_detail.course.name")
    coordinatior_name = serializers.CharField(source='coordinatior.name')
    training_course_detail_name = serializers.CharField(source='training_course_detail.name')
    training_center_address = serializers.CharField(source='training_center.address')


    class Meta:
        model = Batch
        fields = ("id", "batch_name", "course_name", "trainee", "trainer", "coordinatior_name", "training_course_detail_name", "training_center_address")





# class TraineeByAttendence:
#     def __init__(self, trainee_id, attendence):
#         self.trainee_id = trainee_id
#         self.attendence = attendence

# class TraineeByAttendenceSerializer(serializers.Serializer):
#     trainee_id = serializers.PrimaryKeyRelatedField(read_only=True)
#     attendence = serializers.SerializerMethodField()

#     class Meta:
#         model = TraineeByAttendence
#         fields = ['trainee_id', 'attendence']



# class BatchDetailsSerializer(serializers.ModelSerializer):
#     # traineeByattendence = serializers.SerializerMethodField()
#     r =TraineeSerializer(many=True, read_only=True)

#     class Meta:
#         model = Batch
#         fields = ("id", "batch_name", "r")
    
#     def get_traineeByattendence(self, name):
#         trainees = Batch.objects.filter(trainee__name=name)
#         print(trainees)
#         return BatchDetailsSerializer(trainees, many=True).data