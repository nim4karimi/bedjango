from django.shortcuts import render ,HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class home(TemplateView):
    template_name = 'index.html'


