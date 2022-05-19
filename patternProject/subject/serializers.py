from .models import Subject,Lecture,Notes
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Subject
        fields = '__all__'
        

class LectureSerializer(serializers.ModelSerializer):
    # subject = serializers.ReadOnlyField(source = 'Subject.name')
    class Meta:
        model = Lecture
        fields = '__all__'
        

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'