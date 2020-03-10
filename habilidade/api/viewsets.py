from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from habilidade.models import Habilidade
from .serializers import HablidadeSerializer


class HabilidadeViewSet(ModelViewSet):
    serializer_class = HablidadeSerializer

    # Especifica quais métodos o endpoint deve aceitar, se não especificar nada aceita todos (os parâmetros devem ser especifiados em minusculo)
    http_method_names = ['get', 'post','delete','update' ]


    # Paara a autenticação funcionar devo passar no body o parâmetro Authorization e como valor  a palavra Token e o token
    #permission_classes = (IsAuthenticated,)
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)

    # QUANDO O ATRIBUTO queryset NÃO ESTÁ DECLARADO, POSSO SOBRESCREVER A FUNÇÃO
    # get_queryset para  filtrar valores

    # queryset = Habilidade.objects.all()

    def get_queryset(self):
        return Habilidade.objects.filter(ativo=True)

    # sobreescrevendo metodo list (GET geral, e não no detalhe)

    # def list(self, request, *args, **kwargs):
    #     parametroDoHeader = request.META.get("TESTE")
    #     t = request.data
    #     return Response({'t': 12})

    # def create(self, request, *args, **kwargs):
    #     parametroDoHeader = request.META.get("HTTP_HOST", "")
    #     parametro = request.data['usuario']
    #     return Response({'t': parametro})


    #Sobrescrevendo o método de delete para inativar o objeto ao invés de remover do banco de dados.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.ativo = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
