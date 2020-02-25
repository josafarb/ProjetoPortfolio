from django.shortcuts import render
from .validador import *

# Create your views here.
from django.views.generic import TemplateView
from pessoa.models import Pessoa
from habilidade.models import  Habilidade


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        p = Pessoa.objects.first()
        if(p is not None):
            context['pessoa'] = p
            context['habilidade'] =  Habilidade.objects.filter(pessoa = p.id, ativo = True)
        return context

