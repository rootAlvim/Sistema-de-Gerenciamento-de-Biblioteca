from src.biblioteca.usuario import Usuario
U1 = Usuario(
    "Vanessa Camargo Silva Pinto",
    "34562345678",
    "12-11-1999",
    1,
    "Rua joão preto, numero 13, bairro cascalho"
)
print(U1)
print(f'{U1.get_compras()}\n{U1.get_cpf()}\n{U1.get_data_nascimento()}\n{U1.get_emprestimos()}\n{U1.get_endereco()}\n{U1.get_pendencias()}')
