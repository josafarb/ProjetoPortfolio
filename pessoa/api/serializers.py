from rest_framework.serializers import ModelSerializer
from pessoa.models import Pessoa



class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome','sobreNome','dataNascimento','foto')