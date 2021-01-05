from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.
from .forms import ContactForm
class ContactUsView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url= "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
        
