from rest_framework.viewsets import ModelViewSet
from pessoa.models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
