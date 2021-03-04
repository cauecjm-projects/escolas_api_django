from rest_framework import  serializers

from apps.aluno.models import Aluno
from apps.escola.models import Curso, Matricula

from apps.aluno.validates.aluno_validates import  *
from apps.escola.validates.curso_validates import  *

from core.api.v1.serializers import AlunoSerializer


class AlunoSerializer(AlunoSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'rg', 'cpf', 'data_nascimento', 'celular', 'foto']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

    def validate(self, data):
        if 'codigo_curso' in data and not codigo_curso_valido(data['codigo_curso']):
            raise serializers.ValidationError({ "codigo_curso": "Código do curso inválido. O formato deve ser: XXXX_99" })
        if 'nome' in data and not nome_valido(data['nome']):
            raise serializers.ValidationError({ "nome": "O nome do curso deve ter no mínimo 4 caracteres." })
        return data


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaCursosAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ('curso', 'periodo')

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source = 'aluno.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ('aluno', 'periodo')

    def get_periodo(self, obj):
        return obj.get_periodo_display()