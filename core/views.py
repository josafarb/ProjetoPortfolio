from django.shortcuts import render
from .validador import *

# Create your views here.
from django.views.generic import TemplateView
from pessoa.models import Pessoa


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pessoa'] = Pessoa.objects.filter(id=1).first()
        return context

