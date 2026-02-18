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
usuario = f1.get_biblioteca().registrarUsuario(
    "Alvim",
    "12345678909",
    "23-1-1978",
    "rua Chico buarque"
)
f1.get_biblioteca().registrar_Emprestimo(usuario,"12-1-2089")
f1.get_biblioteca().getEmprestimos()[-1].Adicionar_livro(l2,12)
print(f1.get_biblioteca().getEmprestimos()[-1].getLivros())
f1.get_biblioteca().getEmprestimos()[-1].Remover_livro(l2,1)
print(f1.get_biblioteca().getEmprestimos()[-1].getLivros())