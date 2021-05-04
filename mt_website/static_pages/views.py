from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .forms import ContactForm

class Index(TemplateView):
    template_name = 'static_pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context

class ContactEmail(RedirectView, FormMixin):

    pattern_name = 'static_pages:index'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                form.send_email()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'You message was sent to the organizer')
            return self.get(request, *args, **kwargs)
        else:
            messages.error(request, 'An error occured with your message, please contact us directly at: massiliabarbellclub@gmail.com')
            return self.get(request, *args, **kwargs)
