from django.db import models
from home.models import User
# Create your models here.

class Subject(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    student = models.ForeignKey(
<<<<<<< HEAD
        User, on_delete=models.CASCADE, related_name='subject_student'
=======
        User, on_delete=models.CASCADE, related_name='Subject_student'
>>>>>>> 5d425e0c54a5757aa3a27ef1d4b8fa11a4aff803
    )
    pf_name = models.CharField(null=True, blank=True, max_length=20)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idx

class Lecture(models.Model):
    idx = models.AutoField(primary_key=True)
    choice_state = (
        ('ongoing', 'ongoing'),
        ('completed','completed')
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Lecture_student'
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='subject_lecture')
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lecture_student'
    )
    name = models.CharField(max_length=100)
    degree = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    complet_date = models.DateTimeField(null=True, blank=True)
    lecture_time = models.CharField(null=True, blank=True, max_length=20)
    learning_time = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, choices=choice_state)
    video_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.idx

class Notes(models.Model):
    idx = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='notes_lecture')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.idx


    

           