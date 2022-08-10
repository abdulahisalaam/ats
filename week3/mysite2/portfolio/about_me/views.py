from django.shortcuts import render
from django.views.generic.list import ListView
from .models import About_me

# Create your views here.

class IndexView(ListView):
    template_name = 'base.html'
    model = About_me

class AboutView(ListView):
    template_name = 'about.html'
    model = About_me

class PortfolioView(ListView):
    template_name = 'portfolio.html'
    model = About_me
    # context_object_name = "About_me"

    def __str__():
        pass

    # def get_queryset(self, *args, **kwargs):
    #     qs = super(About_me, self).get_queryset(*args, **kwargs)
    #     qs = qs.order_by("-id")
    #     return qs

class DetailsView(ListView):
    template_name = 'portfolio-details.html'
    model = About_me

class ResumeView(ListView):
    template_name = 'resume.html'
    model = About_me

class ContactView(ListView):
    template_name = 'contact.html'
    model = About_me

class ServicesView(ListView):
    template_name = 'services.html'
    model = About_me