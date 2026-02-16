from src.biblioteca.pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento,salario:float,cargo:str):
        super().__init__(nome, cpf, data_nascimento)
        self.__salario = salario
        self.__cargo = cargo

    def get_salario(self):
        return self.__salario
    def get_cargo(self):
        return self.__cargo

    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self.get_cargo()} | Salário: {self.get_salario()}"
