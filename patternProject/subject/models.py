from django.db import models
from home.models import User
# Create your models here.

class Lecture(models.Model):
    choice_state = (
        ('ongoing', 'ongoing'),
        ('completed','completed')
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Lecture_student'
    )
    pf_name = models.CharField(null=True, blank=True, max_length=20)
    subject = models.CharField(null=True, blank=True, max_length=20)
    name = models.CharField(max_length=30)
    degree = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    complet_date = models.DateTimeField(null=True, blank=True)
    lecture_time = models.CharField(null=True, blank=True, max_length=20)
    learning_time = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, choices=choice_state)
    video_id = models.CharField(primary_key=True, max_length=200)
    
    def __str__(self):
        return self.video_id

class Notes(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='notes_lecture', primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.lecture


    

           