from django import forms
from .models import Account, UserProfile
import re


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control'
                                                                 }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
                                    
                                                                 }))
  

    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number', 'email','address','pincode','designation','department', 'password']


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{10}$', str(phone)):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone

    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
        self.fields['pincode'].widget.attrs['placeholder'] = 'Enter Pincode'
        self.fields['designation'].widget.attrs['placeholder'] = 'Enter Designation'
        self.fields['department'].widget.attrs['placeholder'] = 'Enter Department'
         
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number','email' ,'address', 'pincode', 'designation', 'department']
    
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture','city','state','country']
        
    