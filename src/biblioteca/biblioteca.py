from src.biblioteca.acervo import Acervo
from src.biblioteca.funcionario import Funcionario
from src.biblioteca.usuario import Usuario
from src.biblioteca.emprestimo import Emprestimo
from src.validacoes.validacoes import validar_formato_cpf
class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.__emprestimos = []
        self.__acervo = Acervo()
        self.__usuarios = []
        self.__funcionario = None
        self.__idVendas = 0
        self.__idemprestimo = 0
        self.__idusuario = 0
    def getFuncionario(self):
        return self.__funcionario
    def getEmprestimos(self):
        return self.__emprestimos
    def getAcervo(self):
        return self.__acervo
    def getUsuarios(self):
        return self.__usuarios
    
    def __str__(self):
        return f"({self.getFuncionario()}) |{self.getEmprestimos()} |{self.getUsuarios()}"
    
    def getClientePorCpf(self, cpf):
        '''Retorna objeto de cliente caso exista um com o mesmo cpf recebido.'''
        validar_formato_cpf(cpf)
        for cliente in self.__usuarios:
            if cpf == cliente.get_cpf():
                return cliente
            
    def registrarFuncionario(self,nome, cpf, data_nascimento,salario,cargo):
        funcionario = Funcionario(nome,cpf,data_nascimento,salario,cargo,self)
        self.__funcionario = funcionario
        return funcionario

    def registrarUsuario(self, nome, cpf, data_nascimento,endereco):
        self.__idusuario += 1 
        usuario = Usuario(nome,cpf,data_nascimento,self.__idusuario,endereco)
        self.__usuarios.append(usuario)
        return usuario
    
    def registrar_Emprestimo(self,usuario,data_emprestimo):
        self.__idemprestimo += 1 
        emprestimo = Emprestimo(self.__idemprestimo,usuario,data_emprestimo,self)
        self.__emprestimos.append(emprestimo)
        return emprestimo
    
    def excluirUsuario(self,id_usuario):
        lista = self.getUsuarios()
        for n in lista:
            if id_usuario == n.get_id():
                lista.remove(n)
                return True
        raise ValueError('Usuario não encontrado')
    
    def excluirEmprestimo(self,id_emprestimo):
        lista = self.getEmprestimos()
        for n in lista:
            if id_emprestimo == n.getId():
                lista.remove(n)
                return True
        raise ValueError('Emprestimo não encontrado')
    def buscar_usuario(self,id):
        lista = self.getUsuarios()
        for n in lista:
            if id == n.get_id():
                return n
            break

    def consultar_emprestimo(self,usuario,id):
        for n in usuario.get_emprestimos():
            if id == n.getId():
                return n
            break