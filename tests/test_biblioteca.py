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
u = f1.get_biblioteca().registrarUsuario('Chico','12312312312','1-1-1990','Rua joao preto')
print(*f1.get_biblioteca().getUsuarios(),sep='\n')

f1.get_biblioteca().registrar_Emprestimo(u,'1-1-1990')
print(*f1.get_biblioteca().getEmprestimos(),sep='\n')

f1.get_biblioteca().excluirUsuario(1)
print(f1.get_biblioteca().getUsuarios())