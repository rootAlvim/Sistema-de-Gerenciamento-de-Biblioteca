from src.biblioteca.livro import Livro
class Emprestimo:
    def __init__(self,id,usuario,data_emprestimo,biblioteca):
        self.__id = id
        self.__usuario = usuario
        self.__data_emprestimo = data_emprestimo
        self.__livros = []
        self.__data_entrega = '0'
        self.__status = False
        self.__preco_total = 0
        self.__bibilioteca = biblioteca

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
    def getStatus(self):
        if self.__status:
            return f'Finalizado'
        else:
            return f'Pendente'
    def setStatus(self,status):
        self.__status = status
    def getPreco_total(self):
        return self.__preco_total
    
    def __repr__(self):
        return f'Id do Emprestimo: {self.getId()} | Usuario: {self.getUsuario().nome} | Data: {self.getDataEmprestimo()} | Status: {self.getStatus()}'
    
    def Adicionar_livro(self,livro,qntd):
        if self.__preco_total:
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
        if self.__preco_total:
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
        if self.__preco_total:
            raise PermissionError("Emprestimo já finalizado")
        for item in self.__livros: 
            self.__bibilioteca.getAcervo().livro_disponibilidade(item.id,item.quantidade)
        sub = 0
        for item in self.__livros:
            sub += item.preco
        for item in self.__livros:
            self.__bibilioteca.getAcervo().remover_livro_id(item.id, item.quantidade)

        self.__preco_total = sub
        self.__data_entrega = '1-1-1990'
        self.__status = True  
        self.__usuario.get_emprestimos().append(self)
        self.setStatus(False) 
        

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