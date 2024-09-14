from django import forms 
from .models import * 
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}), label='Enter Password')  
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' Re-Enter Password here'}),label='Enter Password') 
    class Meta:
        model = Bloggers 
        fields = '__all__' 
        exclude = ['date_joined','last_login','is_active','is_staff','image'] 
    
    
        widgets = {'email':forms.EmailInput(attrs={"placeholder":'Enter Email here'}),
                  'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name here'}),
                  'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name here'}),
                  'mobile':forms.NumberInput(attrs={'placeholder':'Enter mobile number here'}),
                  'date_of_birth':forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','type':'date'}),
                   'gender':forms.Select(choices=Bloggers.GENDER_CHOICES,attrs={'placeholder':'Select your Gender'}),
                   }
        
        labels = { 'email':'Enter Email ',
                 'first_name':'Enter First Name',
                 'last_name':'Enter  Last Name',
                 'mobile':'Enter  Mobile Number',
                 'date_of_Birth':'Enter  Date of birth',
                 'gender':'Select  Gender'}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
   
class studentPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old Password'}),label='Enter Old Password') 
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New Password'}),label='Enter New Password') 
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm New Password'}),label='Confirm New Password')
    


