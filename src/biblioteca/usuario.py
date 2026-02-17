from src.biblioteca.pessoa import Pessoa
from datetime import datetime
class Usuario(Pessoa):
    def __init__(self, nome:str, cpf:str, data_nascimento:datetime,id:int,endereco:str):
        super().__init__(nome, cpf, data_nascimento)
        self.__id = id
        self.__endereco = endereco
        self.__emprestimos = []
        self.__compras = []
        self.__pendencias = []

    def get_id(self):
        return self.__id
    def get_endereco(self):
        return self.__endereco
    def get_emprestimos(self):
        return self.__emprestimos
    def get_compras(self):
        return self.__compras
    def get_pendencias(self):
        return self.__pendencias
    
    def __str__(self):
        return f"Nome: {self.nome} | Id: {self.get_id()} | Endereço: {self.get_endereco()}"