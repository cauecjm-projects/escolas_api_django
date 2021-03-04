from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('cursos', CursosViewSet)
router.register('matriculas', MatriculasViewSet)

api_urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:pk>/cursos/', ListaCursosAlunoViewSet.as_view()),
    path('cursos/<int:pk>/alunos/', ListaAlunosCursoViewSet.as_view()),
]