from .models import Pessoa

from django.contrib import admin


# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sexo', 'dataNascimento','foto')
