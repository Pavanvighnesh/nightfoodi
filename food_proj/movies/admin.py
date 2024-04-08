from django.contrib import admin
from .models import movie
from food.models import profile

# Register your models here.
#admin.site.unregister(profile)
admin.site.register(movie)