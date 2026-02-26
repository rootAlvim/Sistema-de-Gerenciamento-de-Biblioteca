from src.biblioteca.livro import *
from src.biblioteca.biblioteca import *
from src.biblioteca.emprestimo import *
livro = Livro(
    'João e Maria',
    'Chico Buarque',
    'Moderna',
    12,
    '12-02-1998',
    'Fantasia',
    2.90,
    2
)
blibioteca = Biblioteca('Paulo Freire')
blibioteca.getAcervo().adicionar_livro(livro,12)
Usuario = blibioteca.registrarUsuario(
    "Vanessa Camargo Silva Pinto",
    "34562345678",
    "12-11-1999",
    "Rua joão preto, numero 13, bairro cascalho"
    )
x = blibioteca.registrar_Emprestimo(Usuario,'21-3-1998')
x.Adicionar_livro(livro,2)
x.Adicionar_livro(livro,1)
x.Remover_livro(livro,3)
print(x)