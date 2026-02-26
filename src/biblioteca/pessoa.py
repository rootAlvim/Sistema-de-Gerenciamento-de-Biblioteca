from abc import ABC , abstractmethod
from src.validacoes.validacoes import validar_formato_cpf
from datetime import datetime
class Pessoa(ABC):
    def __init__(self,nome:str,cpf:str,data_nascimento:datetime):
        self.nome = nome
        self.__cpf = validar_formato_cpf(cpf)
        self.__data_nascimento = data_nascimento
        
    @abstractmethod
    def __str__(self):
        return f"Nome: {self.nome} | Cpf: {self.get_cpf()} | Data de Nascimento: {self.get_data_nascimento()}"
    def get_cpf(self):
        '''Retorna Cpf da Pessoa'''
        return self.__cpf
    def get_data_nascimento(self):
        '''Retorna Data de Nascimento da Pessoa'''
        return self.__data_nascimento
    def set_cpf(self,cpf_novo):
            validar_formato_cpf(cpf_novo)
            self.__cpf = cpf_novo
            return True
    
        
    