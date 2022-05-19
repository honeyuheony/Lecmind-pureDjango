from django.contrib import admin
from .models import Subject, Lecture, Notes

# Register your models here.
admin.site.register(Subject)
admin.site.register(Lecture)
admin.site.register(Notes)