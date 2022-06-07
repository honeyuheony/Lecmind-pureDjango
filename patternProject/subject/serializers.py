from home.serializers import UserSerializer
from .models import Lecture,Notes
from rest_framework import serializers
        

# class LectureSerializer(serializers.ModelSerializer):
#     # subject = serializers.ReadOnlyField(source = 'Subject.name')
#     class Meta:
#         model = Lecture
#         fields = '__all__'

class LectureSerializer(serializers.Serializer):
    # subject = serializers.ReadOnlyField(source = 'Subject.name')
    choice_state = (
        ('ongoing', 'ongoing'),
        ('completed','completed')
    )
    student = UserSerializer(required=False)
    pf_name = serializers.CharField(required=False, max_length=20)
    subject = serializers.CharField(required=False, max_length=20)
    name = serializers.CharField(required=False, max_length=30)
    degree = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateField(required=False)
    complet_date = serializers.DateTimeField(required=False, )
    lecture_time = serializers.CharField(required=False, max_length=20)
    learning_time = serializers.CharField(required=False, max_length=20)
    state = serializers.CharField(max_length=20)
    video_id = serializers.CharField(max_length=200)
        

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'