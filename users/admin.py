from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Bloggers) 
class BloggersAdmin(admin.ModelAdmin): 
    list_display = ['id','name','email','mobile'] 


 
    