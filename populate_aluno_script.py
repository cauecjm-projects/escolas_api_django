import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import random

from faker import Faker
from validate_docbr import CPF

from apps.aluno.models import Aluno


def criando_alunos(qtd):
    faker = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(qtd):
        cpf = CPF()
        nome = faker.name()

        aluno = Aluno(
            nome = nome,
            rg = f"{random.randrange(10, 99)}{random.randrange(100, 999)}{random.randrange(100, 999)}{random.randrange(0, 9)}",
            cpf = cpf.generate(),
            data_nascimento = faker.date(),
            email = f"{nome.lower().replace(' ','_')}@{faker.free_email_domain()}",
            celular = f"{random.randrange(10, 21)} 9{random.randrange(4000,9999)}-{random.randrange(4000,9999)}",
        )
        aluno.save()


criando_alunos(50)
print("### Alunos Criados com Sucesso ###")