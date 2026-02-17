from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.livro import Livro
b = Biblioteca('Paolo Guerreiro')
f1 = b.registrarFuncionario('Junior','12312312312','1-1-1990',1222,'Bibliotecario')
l2 = Livro(
    "Cravo da India",
    "Chico Buarque",
    "Moderna",
    102,
    "1-1-1990",
    "Fantasia",
    1.20,
    3
)
f1.get_biblioteca().getAcervo().adicionar_livro(l2,12)
print(f1.get_biblioteca().getAcervo().consultar_acervo())
f1.get_biblioteca().getAcervo().remover_livro_id(4,2)
print(f1.get_biblioteca().getAcervo().consultar_acervo())