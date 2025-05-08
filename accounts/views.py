from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, UserProfileUpdateForm, UserUpdateForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils import timezone

from .models import Account, UserProfile
from .forms import RegistrationForm, UserProfileUpdateForm, UserUpdateForm
from .tasks import send_password_reset_email,send_activation_email_task


    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            pincode = form.cleaned_data['pincode']
            designation = form.cleaned_data['designation']
            department = form.cleaned_data['department']

            username = email.split('@')[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.address = address
            user.pincode = pincode
            user.designation = designation
            user.department = department
            user.save()

            # USER ACTIVATION - Using Celery Task
            current_site = get_current_site(request)
            send_activation_email_task.delay(user.id, current_site.domain)

            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# User Activation View
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated!')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('register')

# User Login
def login(request):
    if request.method == 'POST':
       
        email = request.POST.get ('email')
        password = request.POST.get('password')
        email = request.POST.get['email']
        password = request.POST.get['password']
       
        next_url = request.POST.get('next')

        user = auth.authenticate(request, username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect(next_url if next_url else 'dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    next_url = request.GET.get('next', '')
    return render(request, 'accounts/login.html', {'next': next_url})

# User Logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in updating profile.')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'user': request.user,
    }
    return render(request, 'accounts/dashboard.html', context)

# Password reset request# Password reset request
def forgotPassword(request):
    if request.method == "POST":
        email = request.POST['email']
        
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            current_site = get_current_site(request)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://{current_site.domain}/accounts/resetpassword_validate/{uidb64}/{token}"
            
            send_password_reset_email.delay(user.email, reset_link)
            
            messages.success(request, 'Password reset email has been sent to your email address!')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    
    return render(request, 'accounts/forgotPassword.html')


# Reset password validation

# Validate Reset Password Token
def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link is invalid or expired.')
        return redirect('forgotPassword')

# Reset Password
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            if uid:
                try:
                    user = Account.objects.get(pk=uid)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Password reset successfully!')
                    return redirect('login')
                except Account.DoesNotExist:
                    messages.error(request, 'Something went wrong. Please try again.')
                    return redirect('forgotPassword')
            else:
                messages.error(request, 'Session expired. Please try again.')
                return redirect('forgotPassword')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('resetPassword')

    return render(request, 'accounts/resetPassword.html')
