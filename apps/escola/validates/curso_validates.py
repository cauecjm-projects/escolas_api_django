import re

def codigo_curso_valido(codigo_curso):
    estrutura = "[A-Z]{4}_[0-9]{2}"
    res = re.findall(estrutura, codigo_curso)
    return res

def nome_valido(nome):
    return len(nome) > 3