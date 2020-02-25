from django.db import models
from stdimage import StdImageField
import uuid


class Pessoa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length= 100)
    sobreNome = models.CharField('Sobrenome', max_length= 100)

    SEXO_ESCOLHA = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    sexo = models.CharField('Sexo', max_length=12, choices=SEXO_ESCOLHA)
    dataNascimento = models.DateField('data nascimento')
    pais = models.CharField('País', max_length= 100)
    estado = models.CharField('Estado', max_length=100)
    email = models.EmailField('Email', max_length= 100)
    tempoExperiencia = models.CharField('Tempo experiência', max_length= 100)
    biografia = models.TextField('Sobre mim ')
    foto = StdImageField('Foto', upload_to='pessoa', variations={'tumb': {'width': 524, 'height': 566, 'crop': True}})


