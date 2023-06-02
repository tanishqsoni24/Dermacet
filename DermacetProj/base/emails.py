from django.conf import settings
from django.core.mail import send_mail

# Create Emails Here!

# Account Activation Email

def send_account_activation_email(email, email_token):
    subject = "Account Activation Email"
    email_from = settings.EMAIL_HOST_USER
    message = f"Hi, Click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}" 

    send_mail(subject, message, email_from, [email])

# Forgot Password Email

def send_forgot_password_email(email, email_token):
    subject = "Forgot Password Email"
    email_from = settings.EMAIL_HOST_USER
    message = f"Hi, Click on the link to reset your password http://127.0.0.1:8000/accounts/change-password/{email_token}"

    send_mail(subject, message, email_from, [email])
    return True