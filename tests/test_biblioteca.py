from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.livro import Livro
from src.biblioteca.acervo import Acervo
b = Biblioteca('Paolo Guerreiro')
f1 = b.registrarFuncionario('Junior','12312312312','1-1-1990',1222,'Bibliotecario')
l1 = Livro(
    "Joao Pe de feijao",
    "Chico Buarque",
    "Moderna",
    12,
    "1-1-1997",
    "Fantasia",
    2.90,
    5
)
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
usuario = f1.get_biblioteca().registrarUsuario(
    "Alvim",
    "12345678909",
    "23-1-1978",
    "rua Chico buarque"
)
