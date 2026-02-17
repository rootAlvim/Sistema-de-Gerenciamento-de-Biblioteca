from src.biblioteca.acervo import Acervo
from src.biblioteca.livro import Livro

acervo = Acervo()
l1 = Livro(
    "Joao e Maria",
    "Chico Bento",
    "Moderna",
    1902,
    "1-1-1990",
    "Fantasia",
    1.90,
    9
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
acervo.adicionar_livro(l1,12)
acervo.adicionar_livro(l2,20)
print(acervo.consultar_acervo())
#acervo.remover_livro_id(9)
print(acervo.consultar_acervo())
print(acervo.consultar_livro_nome('joao e maria'))
print(acervo.consultar_livro_id(3))
