from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

    # id = models.CharField(max_length=20,primary_key=True)
    # password = models.CharField(max_length=100)
    # name = models.CharField(default='', max_length=10, null=False, blank=False)
    # email = models.EmailField(default='',max_length=100, null=False, blank=False, unique=True)

class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
                'required': 'True',
            }
        ),
        max_length = 100,
        error_messages={'required': '이메일을 입력해 주세요.',
                        'invalid' : '이미 사용중인 이메일입니다.'}
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'required': 'True',
            }
        ),
        max_length = 10
    )
    id= forms.CharField(
        label='Id',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Id',
                'required': 'True',
            }
        ),
        max_length = 20
    )
    class Meta:
        model = User
        fields = ['name', 'id', 'password1', 'password2', 'email']
    
# class UserForm(ModelForm):
#     # email = forms.EmailField(label="이메일")
#     class Meta:
#         model = User
#         exclude = ['last_login', 'is_active','is_admin','is_superuser']