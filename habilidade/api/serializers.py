from rest_framework.serializers import ModelSerializer
from habilidade.models import Habilidade



class HablidadeSerializer(ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'nome','descricao','ativo','pessoa', 'imagem')