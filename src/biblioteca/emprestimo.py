from src.biblioteca.livro import Livro
class Emprestimo:
    def __init__(self,id,usuario,data_emprestimo):
        self.__id = id
        self.__usuario = usuario
        self.__data_emprestimo = data_emprestimo
        self.__livros = []
        self.__data_entrega = 0

    def getId(self):
        return self.__id
    def getUsuario(self):
        return self.__usuario
    def getLivros(self):
        return self.__livros
    def getDataEmprestimo(self):
        return self.__data_emprestimo
    def getDataEntrega(self):
        return self.__data_entrega
    
    def __repr__(self):
        return f'Id do Emprestimo: {self.getId()} | Usuario: {self.getUsuario().nome} | Data: {self.getDataEmprestimo()}'
    
    def Adicionar_livro(self,livro,qntd):
        if self.__data_entrega:
            raise PermissionError("Emprestimo ja finalizado")
        if int(qntd) <= 0:
            raise ValueError('Quantidade deve ser maior que 0')
        
        for item in self.__livros:   
            if livro.get_id() == item.id:
                item.quantidade += qntd
                return True

        self.__livros.append(
            Item(
                livro.titulo,
                livro.autor,
                livro.editora,
                livro.edicao,
                livro.ano_publicacao,
                livro.genero,
                livro.get_preco(),
                livro.get_id(),
                int(qntd)
            )
        )

    def Remover_livro(self,livro,qntd):
        if self.__data_entrega:
            raise PermissionError("Emprestimo já finalizado")
        if int(qntd) <= 0:
            raise ValueError("Quantidade deve ser maior que 0")

        for item in self.__livros:
            if livro.get_id() == item.id:
                if item.quantidade < qntd:
                    raise ValueError("Quantidade excede valor disponível para remoção")
                item.quantidade -= qntd
                return True
        raise ValueError("Livro não está adicionado no emprestimo")
    
    def Finalizar_emprestimo(self):
        if self.__data_entrega:
            raise PermissionError("Emprestimo já finalizado")
        

class Item:
    def __init__(self,titulo,autor,editora,edicao,ano_publicacao,genero,preco,id,quantidade):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.preco = preco
        self.id = id
        self.quantidade = quantidade
    def __repr__(self):
        return f"Id={self.id}, Nome={self.titulo}, Preço={self.preco}, Quantidade: {self.quantidade}"