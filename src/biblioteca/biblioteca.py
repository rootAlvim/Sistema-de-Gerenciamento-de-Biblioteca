from src.biblioteca.acervo import Acervo
from src.biblioteca.funcionario import Funcionario
from src.biblioteca.usuario import Usuario
class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.__emprestimos = []
        self.__acervo = Acervo()
        self.__usuarios = []
        self.__idVendas = 0
        self.__idemprestimo = 0
        self.__idusuario = 0
    def getEmprestimos(self):
        return self.__emprestimos
    def getAcervo(self):
        return self.__acervo
    def getUsuarios(self):
        return self.__usuarios
    
    def registrarFuncionario(self,nome, cpf, data_nascimento,salario,cargo):
        funcionario = Funcionario(nome,cpf,data_nascimento,salario,cargo,self)
        return funcionario

    def registrarUsuario(self, nome, cpf, data_nascimento,endereco):
        self.__idusuario += 1 
        usuario = Usuario(nome,cpf,data_nascimento,self.__idusuario,endereco)
        return usuario
    
    def registrar_Emprestimo(self):
        pass