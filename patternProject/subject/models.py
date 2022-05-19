from django.db import models
from home.models import User
# Create your models here.

class Subject(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student'
    )
    pf_name = models.CharField(null=True, blank=True, max_length=20)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Lecture(models.Model):
    choice_state = (
        ('before', 'before'),
        ('ongoing', 'ongoing'),
        ('completed','completed')
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='subject_lecture')
    name = models.CharField(max_length=30)
    degree = models.IntegerField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    complet_date = models.DateField(auto_now_add=True)
    lecture_time = models.CharField(max_length=20)
    learning_time = models.CharField(max_length=20)
    state = models.CharField(max_length=20, choices=choice_state)
    url = models.URLField(primary_key=True, max_length=200)
    
    def __str__(self):
        return self.url

class Notes(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='notes_lecture', primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.lecture


    

           