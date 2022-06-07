from django.db import models
from subject.models import Lecture

# Create your models here.


class Review_section(models.Model):
    review_section_idx = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='review_section_lecture')
    section_start = models.CharField(max_length=20)
    section_end = models.CharField(max_length=20)
    
    def __str__(self):
        return self.review_section_idx

class Analysis(models.Model):
    anlysis_idx = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='analysis_lecture')
    
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
        return str(self.interaction_idx)

class Review_section(models.Model):
    review_section_idx = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='reviewsection_lecture')
    section_start = models.CharField(max_length=20)
    section_end = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.review_section_idx)