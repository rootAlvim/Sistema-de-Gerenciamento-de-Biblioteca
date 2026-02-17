
class Emprestimo:
    def __init__(self,id,usuario,data_emprestimo):
        self.__id = id
        self.__usuario = usuario
        self.__data_emprestimo = data_emprestimo
        self.__livros = []

    def getId(self):
        return self.__id
    def getUsuario(self):
        return self.__usuario
    def getLivros(self):
        return self.__livros
    def getDataEmprestimo(self):
        return self.__data_emprestimo
    