from django.contrib import admin
from .models import Analysis, Interaction, Review_section

# Register your models here.
admin.site.register(Analysis)
admin.site.register(Interaction)
admin.site.register(Review_section)