class Livro:
    def __init__(self,titulo,autor,editora,edicao,ano_pulicacao,genero,preco,id):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.edicao = edicao
        self.ano_publicacao = ano_pulicacao
        self.genero = genero 
        self.__preco = preco
        self.__id = id
    
    def get_preco(self):
        return self.__preco
    
    def get_id(self):
        return self.__id
    
    def __repr__(self):
        return f"Id={self.get_id()}, Nome={self.titulo}, Preço={self.get_preco()}, Quantidade"
    
    def __str__(self):
        return (
            f"ID: {self.__id}\n"
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Editora: {self.editora}\n"
            f"Edição: {self.edicao}\n"
            f"Ano de Publicação: {self.ano_publicacao}\n"
            f"Gênero: {self.genero}\n"
            f"Preço: R$ {self.__preco:.2f}"
        )