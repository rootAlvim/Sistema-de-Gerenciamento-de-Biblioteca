from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.acervo import Acervo
from src.biblioteca.emprestimo import Emprestimo
from src.biblioteca.funcionario import Funcionario
from src.biblioteca.livro import Livro
from src.biblioteca.pessoa import Pessoa
from src.biblioteca.usuario import Usuario
import os
import time
import random
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            limpar_tela()
def ler_quebrado(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            

B = Biblioteca("Paulo Freire")
def carregar_dados_iniciais(B):
    l1 = Livro("Dom Casmurro", "Machado", "Saraiva", 1, "1899", "Romance", 30.0, 5)
    l2 = Livro("Python POO", "Alguém", "Tech", 2, "2020", "Tecnico", 50.0, 3)
    B.registrarUsuario(
    "Vanessa",
    "12345678909",
    "12-1-1001",
    "Rua joão preto, numero 13, bairro cascalho"
    )
    B.getAcervo().adicionar_livro(l1, 10)
    B.getAcervo().adicionar_livro(l2, 5)
    f = B.registrarFuncionario(
        "Clara",
        "12345678909",
        "1-1-1990",
        1.200,
        "Bibliotecario",
    )
carregar_dados_iniciais(B)
f = B.getFuncionario()

def limpar_tela():
        """Limpa o console."""
        os.system('cls' if os.name == 'nt' else 'clear')   

def funcionario():

    def adicionar_livro():
        limpar_tela()
        print("=============== CADRASTAR LIVRO =============== ")
        id_livro = 1
        titulo = str(input("Digite o Título do Livro: "))
        autor = str(input("Digite o Autor do Livro: "))
        editora = str(input("Digite a Editora do Livro: "))
        edicao = ler_inteiro("Digite a Edição do Livro: ")
        ano_publi = ler_inteiro("Digite o Ano de Publicação do Livro: ")
        genero = str(input("Digite o Gênero do Livro: "))
        preco = ler_quebrado("Digite o Preço do Livro: ")
        qntd = ler_inteiro("Digite a Quantidade: ")

        livro = Livro(titulo, autor, editora, edicao, ano_publi, genero, preco, id_livro)
        id_livro += 1
        f.get_biblioteca().getAcervo().adicionar_livro(livro, qntd)

        input("\nPressione Enter para voltar ao menu...")

    def remover_livro():
        limpar_tela()
        print("=============== REMOVER LIVRO =============== ")
        opc = input("Remover Livro por(Nome/Id): ").lower() 
        if opc == "id":
            id = ler_inteiro("Digite o id: ")
            qntd = ler_inteiro("Digite a Quantidade: ")
            f.get_biblioteca().getAcervo().remover_livro_id(id, qntd)
            input("\nPressione Enter para voltar ao menu...")
        elif opc == "nome":
            nome = str(input("Digite o nome do livro: "))
            qntd = ler_inteiro("Digite a Quantidade: ")
            f.get_biblioteca().getAcervo().remover_livro_nome(nome, qntd)
            input("\nPressione Enter para voltar ao menu...")
        else:
            print("Opção inválida!")
            input("\nPressione Enter para voltar ao menu...")
    def buscar_livro():
        limpar_tela()
        opc = input("Buscar Livro por(Nome/Id): ".lower())
        if opc == "nome":
            nome = str(input("Digite o Nome do Livro: "))
            print(f.get_biblioteca().getAcervo().consultar_livro_nome(nome))
            input("\nPressione Enter para voltar ao menu...")
        elif opc == "id":
            id = ler_inteiro("Digite o Id do Livro: ")
            print(f.get_biblioteca().getAcervo().consultar_livro_id(id))
            input("\nPressione Enter para voltar ao menu...")
        else:
            print("Opção inválida!")
            input("\nPressione Enter para voltar ao menu...")
    def consultar_acervo():
        limpar_tela()
        acervo = f.get_biblioteca().getAcervo().consultar_acervo()
        print(*(f"{k}: {v}" for k, v in acervo.items()), sep='\n')    
        input("\nPressione Enter para voltar ao menu...")
    def consultar_usuario():
        limpar_tela()
        id = ler_inteiro("digite id ")
        usuario = B.buscar_usuario(id)
        while True:
            limpar_tela()
            print(f"-" * 45)
            print(f"|             FICHA DO USÚARIO              |") 
            print("-" * 45)
            print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
            print("-" * 45)
            print(f'| {'ID':<15} | {usuario.get_id():<23} |')
            print(f'| {'NOME':<15} | {usuario.nome:<23} |')
            print(f'| {'CPF':<15} | {usuario.get_cpf():<23} |')
            print(f'| {'NASCIMENTO':<15} | {usuario.get_data_nascimento():}              | ')
            print(f'| {'Nº DE EMPRESTIMOS ':<15} | {len(usuario.get_emprestimos()):<25} |')
            print(f"-" * 45)
            opc = input("Deseja Listar Emprestimos do usúario(S/N): ").lower()
            if opc ==  "s":
                print(*usuario.get_emprestimos(), sep='\n')   
                break

        input("\nPressione Enter para voltar ao menu...")
    def realizar_emprestimo():
        limpar_tela()
        cpf = input("Digite o cpf do usuario: ")
        if f.get_biblioteca().getClientePorCpf(cpf) is None:
            print("Usuario não cadrastado")
            limpar_tela()
            nome = str(input("Digite o nome: "))
            cpf = str(input("Digite o cpf: "))
            data_nascimento = str(input("Digite a data de nascimento: "))
            endereco = str(input("endereco: "))
            usuario = f.get_biblioteca().registrarUsuario(nome,cpf,data_nascimento,endereco)
        else:
            usuario = f.get_biblioteca().getClientePorCpf(cpf)
        emprestimo = f.get_biblioteca().registrar_Emprestimo(usuario,'1-1-1990')
        nome = str(input("Digite o Nome do Livro: "))
        livro,_  = B.getAcervo().consultar_livro_nome(nome)
        qntd = ler_inteiro("Digite a quantidade: ")
        emprestimo.Adicionar_livro(livro,qntd)
        emprestimo.Finalizar_emprestimo()
        input("\nPressione Enter para voltar ao menu...")
    def consultar_emprestimo():
        id = ler_inteiro("Digite o id: ")
        print(B.consultar_emprestimo(id))
        input("\nPressione Enter para voltar ao menu...")
    def menu():

        limpar_tela()
        print(f"=" * 40)
        print(f"    Bem Vindo {f.nome} ")
        print(f"=" * 40 + f"")

 

       

        print(f"\n------------------  ACERVO  -------------------")
        print(" [1]  Adicionar Livro ao Acervo")
        print(" [2]  Remover Livro do Acervo")
        print(" [3]  Buscar Livro")
        print(" [4]  Consultar Acervo")
        print("-" * 40)
        print(f"\n------------------    EMPRÉSTIMO OU COMPRA  -------------------")
        print(" [5]  Realizar Emprestimo")
        print(" [6]  Realizar Compra")
        print(" [7]  Consultar Usúario")
        print(" [8]  Consultar Empréstimo")
        print("-" * 40)
        print(f" [0]  Logout")
        print("-" * 40)

    while True:

        menu() 
        opcao = input(str("Escolha uma opção: "))
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            remover_livro()
        elif opcao == "3":
            buscar_livro()
        elif opcao == '4':
            consultar_acervo()
        elif opcao == '5':
            realizar_emprestimo()
        elif opcao == '7':
            consultar_usuario()
        elif opcao == '8':
            consultar_emprestimo()
        elif opcao == '0':
            print("\nSaindo do menu... Até logo!")
            time.sleep(1)
            break
        else:
                print("\nOpção inválida!")
                time.sleep(1)
if __name__ == "__main__":
        

    while True:
            limpar_tela()
            print("=" * 40)
            print("     Biclioteca Paulo Freire")
            print("=" * 40)
            print("\n[1] Entrar no sistema (Cadastrar/Login Gerente)")
            print("[0] Encerrar Programa")
            opc = input(str("\nEscolha uma opção: "))

            if opc == "0":
                print("\nEncerrando sistema... Até logo!")
                break # Sai do loop principal emprestimo termina o programa

            if opc == "1":
                limpar_tela()
                funcionario()
                break