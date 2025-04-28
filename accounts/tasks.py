from celery import shared_task
from django.core.mail import send_mail

from .models import Account

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

# Task to send a password reset email
@shared_task
def send_password_reset_email(user_email, reset_link):
    subject = "Reset Your Password"
    message = f"Click the link below to reset your password:\n{reset_link}"
    send_mail(subject, message, 'no-reply@shaftseal.com', [user_email])
    
# tasks.py




@shared_task
def send_activation_email_task(user_id, domain):
    try:
        user = Account.objects.get(pk=user_id)
        mail_subject = "Activate your account"
        message = render_to_string('accounts/account_verification_email.html', {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })

        to_email = user.email
        send_email = EmailMessage(
            mail_subject,
            message,
            to=[to_email]
        )
        send_email.send()
        return True
    except Account.DoesNotExist:
        return False

