from tabnanny import verbose
from django.db import models
from coordinatiors.models import Coordinatior
from training.models import TrainingCourseDetail, TrainingCenter
from trainee.models import Trainee
from trainer.models import Trainer

# Create your models here.
class Batch(models.Model):
    batch_name = models.CharField(max_length=200)
    trainee = models.ManyToManyField(Trainee)
    trainer = models.ManyToManyField(Trainer)
    coordinatior = models.ForeignKey(Coordinatior, on_delete=models.CASCADE)
    training_course_detail = models.ForeignKey(TrainingCourseDetail, on_delete=models.CASCADE, related_name='training_course_detail_rel')
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="course year")
    end_date = models.DateField()
    
    
    def __str__(self):
        return self.batch_name

    @property
    def year(self):
        return self.start_date.year

    @property
    def course_name(self):
        return self.training_course_detail.course.name

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'
        db_table = 'batch'


