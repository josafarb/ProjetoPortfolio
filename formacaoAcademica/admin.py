from django.contrib import admin
from .models import FormacaoAcademica
# Register your models here.

@admin.register(FormacaoAcademica)
class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'descricao', 'ativo')
