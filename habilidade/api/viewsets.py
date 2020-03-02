from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from habilidade.models import Habilidade
from .serializers import HablidadeSerializer


class HabilidadeViewSet(ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HablidadeSerializer
