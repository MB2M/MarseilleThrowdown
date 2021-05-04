from django import forms
from django.core.mail import send_mail
import os

from django.http.response import BadHeaderError

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    def send_email(self):
        sender_name = self.cleaned_data['name']
        sender_email = self.cleaned_data['email']
        sender_message = self.cleaned_data['message']
        subject = sender_name + ' sent you a new message'
        message =  'Hello, you received a new message from ' + sender_name + ' (' + sender_email + '):\n\n' + sender_message
        send_mail(
            subject,
            message,
            os.environ.get('EMAIL_HOST_USER'),
            [os.environ.get('CONTACT_DEST')],
            fail_silently=False,
        )

