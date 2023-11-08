from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import UserType,Artist,Client,TvChannel,RadioChannel

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    class Meta:
        model = UserType
        fields = ('username','email','first_name','last_name', 'password1', 'password2','TYPE_CHOICES')
        
        
class EditProfileForm(UserChangeForm):    
       first_name = forms.CharField(label="First Name")
       last_name = forms.CharField(label="Last Name")
       image = forms.ImageField()
        
       class Meta:
        model = UserType
        fields = ('username','first_name','last_name','email','image','TYPE_CHOICES')

      