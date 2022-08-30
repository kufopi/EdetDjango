from django.forms import ModelForm
from .models import User,UniversityStaff,Postgrad
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['staff_id','first_name','middle_name','surname','gender','blood_group','category','passport']
       
# Create a ProfileUpdateForm to update image
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name','middle_name','surname','blood_group','passport']

class UniversityStaffForm(forms.ModelForm):
    
    class Meta:
        model = UniversityStaff
        fields = ['session','designation']


class PostgradForm(forms.ModelForm):
    
    class Meta:
        model = Postgrad
        fields = ['session','department','level']

