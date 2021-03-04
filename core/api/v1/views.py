from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.aluno.models import Aluno

from core.api.views import BaseViewSet
from .serializers import AlunoSerializer


class AlunosViewSet(BaseViewSet):
    """ Exibindo todos os registros de Aluno """

    queryset = Aluno.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf', 'email']
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = AlunoSerializer
