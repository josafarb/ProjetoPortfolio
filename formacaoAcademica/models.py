from django.db import models
from django.db.models import ForeignKey

from pessoa.models import  Pessoa
# Create your models here.

class FormacaoAcademica(models.Model):
    instituicao = models.CharField('Instituição', max_length=100)
    inicio = models.DateField('Início')
    fim = models.DateField('Fim',blank=True,null=True)
    descricao = models.TextField('Descrição', max_length=500)
    ativo = models.BooleanField('Ativo', default=True)
    curso = models.CharField('Curso', max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True, null=True)

    def periodo(self):
        if(self.fim is None):
            return self.inicio.strftime('%Y') + ' - até o momento '

        return self.inicio.strftime('%Y') + ' - ' + self.fim.strftime('%Y')
    def __str__(self):
        return self.instituicao
