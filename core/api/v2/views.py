from rest_framework import viewsets, generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.aluno.models import Aluno
from apps.escola.models import Curso, Matricula

from core.api.views import BaseViewSet
from core.api.v1.views import AlunosViewSet

from .serializers import ( 
    AlunoSerializer, CursoSerializer,
    MatriculaSerializer, ListaCursosAlunoSerializer,
    ListaAlunosCursoSerializer
)


class AlunosViewSet(AlunosViewSet):
    """ Exibindo todos os registros de Aluno """
    
    search_fields = ['nome','cpf']
    serializer_class = AlunoSerializer


class CursosViewSet(BaseViewSet):
    """ Exibindo todos os registros de Cursos """

    queryset = Curso.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','codigo_curso', 'nivel']
    filterset_fields = ['ativo']
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class MatriculasViewSet(BaseViewSet):
    """ Exibindo todos os registros de Matrículas """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put']

    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)


class ListaCursosAlunoViewSet(generics.ListAPIView):
    """ Listando os registros de Matrículas de um Aluno """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaCursosAlunoSerializer


class ListaAlunosCursoViewSet(generics.ListAPIView):
    """ Listando os registros de Alunos de um Curso """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosCursoSerializer
    