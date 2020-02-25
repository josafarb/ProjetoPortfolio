from django.db import models
from django.db.models import ForeignKey

from pessoa.models import Pessoa


# Create your models here.
from stdimage import StdImageField


class Habilidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    imagem = StdImageField('Foto', upload_to='habilidade', variations={'tumb': {'width': 100, 'height': 100, 'crop': True}})
    ativo = models.BooleanField('Ativo', default=True)
    pessoa = ForeignKey(Pessoa, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nome;
