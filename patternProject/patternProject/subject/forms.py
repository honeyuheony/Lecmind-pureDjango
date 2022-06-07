from django import forms


from .models import Subject, Lecture, Notes
from home.models import User

# class Subject(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = '__all__'

class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'