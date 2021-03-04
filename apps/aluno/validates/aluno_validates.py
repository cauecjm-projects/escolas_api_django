import re
from validate_docbr import CPF

def nome_valido(nome):
    return bool(nome and nome.strip())

def rg_valido(rg):
    return len(rg) == 9

def cpf_valido(cpf):
    validar_cpf = CPF()
    return validar_cpf.validate(cpf)

def celular_valido(celular):
    estrutura = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    res = re.findall(estrutura, celular)
    return res