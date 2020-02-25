from django.contrib import admin
from .models import ExperienciaProfissiona

# Register your models here.

@admin.register(ExperienciaProfissiona)
class ExperienciaProfissionaAdmin(admin.ModelAdmin):
    list_display = ('empresa','inicio', 'fim')
