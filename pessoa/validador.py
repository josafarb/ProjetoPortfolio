from django.core.exceptions import ValidationError
import time


def validarDataDeNascimento(value):
    anoAtual = int(time.strftime('%Y'))
    anoNascimento = int(value.strftime("%Y"))

    if ((anoAtual - anoNascimento) < 18):
        raise ValidationError(
            'A pessoa deve ter uma idade maior ou igual a 18 anos',
            params={'value': value},
        )


