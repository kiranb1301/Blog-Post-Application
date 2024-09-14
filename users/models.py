from django.db import models
from django.contrib.auth.models import User , PermissionsMixin
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.hashers import make_password,check_password
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.core.validators import FileExtensionValidator

class Bloggers(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    image = models.ImageField(default='default.jpg', upload_to='profile', validators=[
                              FileExtensionValidator(['png', 'jpg'])])
    name = models.CharField(max_length=50,default=None,blank=False) 
    email = models.EmailField(default=None,blank=False,null=False,unique=True) 
    mobile = models.BigIntegerField(null=False,blank=False) 
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    password = models.CharField(max_length=128,default=None,blank=False) 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] 
    
    def update_last_login(self):
        self.last_login = timezone.now() 
        self.save() 
    @property
    def is_authenticated(self):
        return True 
    
    def set_password(self,raw_password): 
        self.password = make_password(raw_password) 
        self.save() 
    
    def check_password(self,raw_password):
        return check_password(raw_password,self.password) 
    
    
    
    def has_perm(self, perm, obj=None):
        return self.is_active and not self.is_staff

    def has_module_perms(self, app_label):
        return True
    
    def get_username(self):
        return self.email

    def __str__(self):
        return self.name