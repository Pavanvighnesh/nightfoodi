from django.contrib import admin
from .models import item,profile
from movies.models import movie

# Register your models here.

#admin-modifications
admin.site.site_header='FOODI APP'
admin.site.site_title='foodi_app'
admin.site.index_title='Managing  Food-items'

class ItemsAdmin(admin.ModelAdmin):
    list_display= ( 'item_name', 'item_desc', 'item_price')
    search_fields=['item_name']

admin.site.register(item,ItemsAdmin)
admin.site.register(profile)
