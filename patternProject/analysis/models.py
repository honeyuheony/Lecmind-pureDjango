from django.db import models
from subject.models import Lecture

# Create your models here.

class Analysis(models.Model):
    anlysis_idx = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='analysis_lecture')
    concentration_rate = models.FloatField()
    review_section = models.CharField(max_length=20)
    
    def __str__(self):
        return self.anlysis_idx

class Interaction(models.Model):
    interaction_idx = models.AutoField(primary_key=True)
    EVENT = (
        ('pause','pause'),
        ('redo','redo'),
        ('fast_forward','fast_forward'),
        ('rewind','rewind'),
    )
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='interaction_lecture')
    interaction_type = models.CharField(choices=EVENT, max_length=20)
    interaction_time_real = models.CharField(max_length=20)
    interaction_time_lecture = models.CharField(max_length=20)
    
    def __str__(self):
        return self.interaction_idx