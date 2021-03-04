from rest_framework import serializers

from apps.aluno.models import Aluno
from apps.aluno.validates.aluno_validates import  *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento']

    def validate(self, data):
        if 'nome' in data and not nome_valido(data['nome']):
            raise serializers.ValidationError({ "nome": "O nome deve ter somente letras." })
        if 'rg' in data and not rg_valido(data['rg']):
            raise serializers.ValidationError({ "rg": "O RG deve ter 9 dígitos." })
        if 'cpf' in data and not cpf_valido(data['cpf']):
            raise serializers.ValidationError({ "cpf": "Número de CPF inválido." })
        if 'celular' in data and not celular_valido(data['celular']):
            raise serializers.ValidationError({ "celular": "Número de celular inválido. O formato deve ser: (xx) xxxxx-xxxxx" })
        return data
