from django.contrib import admin
from .models import TrabalhosRealizados
# Register your models here.

@admin.register(TrabalhosRealizados)
class TrabalhosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('nome',)