from django.contrib import admin
from .models import item,profile
from movies.models import movie

# Register your models here.
admin.site.register(item)
admin.site.register(profile)

#admin-modifications
admin.site.site_header='FOODI APP'
admin.site.site_title='foodi_app'
admin.site.index_title='Managing  Food-items'
