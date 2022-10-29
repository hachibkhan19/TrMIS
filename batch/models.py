from tabnanny import verbose
from django.db import models
from coordinatiors.models import Coordinatior
from training.models import TrainingCourseDetail, TrainingCenter
from trainee.models import Trainee

# Create your models here.
class Batch(models.Model):
    batch_name = models.CharField(max_length=200)
    trainee = models.ManyToManyField(Trainee, through='BatchTrainee')
    coordinatior = models.ForeignKey(Coordinatior, on_delete=models.CASCADE)
    training_course_detail = models.ForeignKey(TrainingCourseDetail, on_delete=models.CASCADE, related_name='training_course_detail_rel')
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.batch_name

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'
        db_table = 'batch'

    
class BatchTrainee(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    # date_joined = models.DateField()

    class Meta:
        db_table = 'batch_trainee'

