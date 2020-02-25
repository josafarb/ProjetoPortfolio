from django.db import models
from django.db.models import ForeignKey
from stdimage import StdImageField

from pessoa.models import  Pessoa
# Create your models here.

class TrabalhosRealizados(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    ativo = models.BooleanField('Ativo', default=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True, null=True)
    imagem = StdImageField('Foto', upload_to='trabalhos_realizados', variations={'tumb': {'width': 500, 'height': 334, 'crop': True}})
    dataCriacao = models.DateField('Data de criação')
    link = models.CharField('Link', max_length=100,blank=True, null= True)

    def __str__(self):
        return self.nome
