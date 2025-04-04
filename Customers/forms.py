from django import forms
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, CustomerProfile

# Admin User Creation Form (for Django Admin)
class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_no']

# User Registration Form (Frontend)
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )

    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Invalid phone number.")
    phone_no = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_no', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            if not self.instance.pk:  # Allow editing existing users in Admin
                raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash password before saving
        if commit:
            user.save()
        return user

# Customer Profile Form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['customer_name', 'address', 'pincode', 'designation', 'department']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Customer Name', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Pincode', 'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Designation', 'class': 'form-control'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department', 'class': 'form-control'}),
        }

# Login Form (Email or Phone Authentication)
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email or Phone Number', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        User = get_user_model()
        user = None

        # Check if the input is an email or phone number
        if username:
            if username.isdigit() and len(username) == 10:  # Phone number login
                try:
                    user_obj = User.objects.get(phone_no=username)
                    user = authenticate(username=user_obj.email, password=password)  # Authenticate using email
                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid phone number or password.")
            else:  # Email login
                user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Invalid login credentials.")

        return cleaned_data
