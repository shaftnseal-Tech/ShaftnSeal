from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, CustomerProfileForm, LoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = CustomerProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')

    else:
        user_form = UserRegistrationForm()
        profile_form = CustomerProfileForm()

    return render(request, 'Customers/CustomerRegister.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']  # Email or phone number
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')

                # Handle next parameter
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('home')

            else:
                form.add_error(None, "Invalid email/phone or password")  # Adds error to form, not messages

    else:
        form = LoginForm()

    return render(request, 'Customers/CustomerLogin.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')
