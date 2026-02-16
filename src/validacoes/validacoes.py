import re 
def validar_formato_cpf(cpf: str):
    padrao = r"^\d{3}(\.?\d{3}){2}-?\d{2}$"
    if re.match(padrao, cpf):
        return cpf
    raise ValueError("Formato de CPF incorreto")
