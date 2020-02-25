from django.contrib import admin
from .models import Habilidade

# Register your models here.

@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo')
