from django import forms
from .models import Neighborhood,Profile,Business,Notice,HealthCenter,Police
from cloudinary.models import CloudinaryField

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields=['hood_name','location','population']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['prof_pic','bio']
        
        
class SubmitBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['bsns_name','bsns_email']
        

class ShareNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['user', 'neighborhood']
        

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']
        
        
class AddNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user']
        
class JoinNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['neighborhood']