from django.shortcuts import redirect, render
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormMixin
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
            form.send_email()
            print('mailing OK')
            return self.get(request, *args, **kwargs)
        else:
            print('mailing error')
            return self.get(request, *args, **kwargs)
