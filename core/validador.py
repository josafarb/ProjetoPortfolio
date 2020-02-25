from pessoa.models import  Pessoa

def existePessoaCadastrada(self):
    try:
        Pessoa.objects.get(id=1)
    except:
        return False

    return True