from django.contrib import admin
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    
    
admin.site.register(PostModel,PostModelAdmin) 
admin.site.register(Comment)