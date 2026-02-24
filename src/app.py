import tkinter as tk
from tkinter import ttk, messagebox
from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.livro import Livro

# ==============================
# Inicialização do sistema
# ==============================

B = Biblioteca("Paulo Freire")

def carregar_dados_iniciais():
    l1 = Livro("Dom Casmurro", "Machado de Assis", "Saraiva", 1, "1899", "Romance", 30.0, 1)
    l2 = Livro("Python POO", "Alguém", "Tech", 2, "2020", "Técnico", 50.0, 2)

    B.getAcervo().adicionar_livro(l1, 10)
    B.getAcervo().adicionar_livro(l2, 5)

    B.registrarFuncionario(
        "Clara",
        "12345678909",
        "01-01-1990",
        1200,
        "Bibliotecário"
    )

carregar_dados_iniciais()
f = B.getFuncionario()

# ==============================
# Interface Tkinter (Melhorada)
# ==============================

def centralizar_janela(janela, largura, altura):
    """Função utilitária para centralizar a janela na tela do usuário"""
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def abrir_menu_funcionario():
    # Oculta a janela principal
    root.withdraw()

    janela = tk.Toplevel(root)
    janela.title("Menu do Funcionário - Sistema Biblioteca")
    centralizar_janela(janela, 600, 500)
    
    # Se o usuário fechar no "X", volta para a tela principal
    janela.protocol("WM_DELETE_WINDOW", lambda: fazer_logout(janela))

    # Estilo e Cabeçalho
    lbl_titulo = ttk.Label(janela, text=f"Bem-vindo(a), {f.nome}", font=("Arial", 16, "bold"))
    lbl_titulo.pack(pady=15)

    # Frame para exibir os dados (Acervo)
    frame_acervo = ttk.LabelFrame(janela, text="Acervo Atual")
    frame_acervo.pack(padx=20, pady=10, fill="both", expand=True)

    # Scrollbar para o texto do acervo
    scroll = ttk.Scrollbar(frame_acervo)
    scroll.pack(side="right", fill="y")
    
    texto = tk.Text(frame_acervo, width=60, height=12, yscrollcommand=scroll.set, font=("Consolas", 10))
    texto.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    scroll.config(command=texto.yview)

    # Funções do Menu
    def consultar_acervo():
        texto.delete("1.0", tk.END)
        acervo = f.get_biblioteca().getAcervo().consultar_acervo()
        
        if not acervo:
            texto.insert(tk.END, "O acervo está vazio.\n")
            return

        for k, v in acervo.items():
            texto.insert(tk.END, f"📌 {k}: {v}\n")
            texto.insert(tk.END, "-" * 50 + "\n")

    def tela_adicionar_livro():
        # Cria uma subtela para preencher os dados do livro
        janela_add = tk.Toplevel(janela)
        janela_add.title("Cadastrar Novo Livro")
        centralizar_janela(janela_add, 350, 400)
        janela_add.grab_set() # Foca nesta janela

        ttk.Label(janela_add, text="Título:").pack(pady=(10, 0))
        ent_titulo = ttk.Entry(janela_add, width=30)
        ent_titulo.pack(pady=2)

        ttk.Label(janela_add, text="Autor:").pack(pady=(5, 0))
        ent_autor = ttk.Entry(janela_add, width=30)
        ent_autor.pack(pady=2)

        ttk.Label(janela_add, text="Ano de Publicação:").pack(pady=(5, 0))
        ent_ano = ttk.Entry(janela_add, width=30)
        ent_ano.pack(pady=2)

        ttk.Label(janela_add, text="Quantidade em Estoque:").pack(pady=(5, 0))
        ent_qtd = ttk.Entry(janela_add, width=30)
        ent_qtd.pack(pady=2)

        def salvar_livro():
            titulo = ent_titulo.get()
            autor = ent_autor.get()
            ano = ent_ano.get()
            qtd_str = ent_qtd.get()

            # Validação básica
            if not titulo or not autor or not qtd_str.isdigit():
                messagebox.showerror("Erro", "Preencha todos os campos corretamente (Quantidade deve ser número).", parent=janela_add)
                return

            # Cria o objeto com os dados reais e alguns fixos para simplificar
            novo = Livro(titulo, autor, "Editora Padrão", 99, ano, "Geral", 50.0, 99)
            f.get_biblioteca().getAcervo().adicionar_livro(novo, int(qtd_str))
            
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso!", parent=janela_add)
            consultar_acervo() # Atualiza a lista automaticamente
            janela_add.destroy() # Fecha a janela de cadastro

        ttk.Button(janela_add, text="Salvar Livro", command=salvar_livro).pack(pady=20)

    def fazer_logout(janela_atual):
        janela_atual.destroy()
        root.deiconify() # Mostra a janela principal novamente

    # Frame para botões de ação
    frame_botoes = ttk.Frame(janela)
    frame_botoes.pack(pady=10)

    ttk.Button(frame_botoes, text="🔄 Consultar Acervo", width=20, command=consultar_acervo).grid(row=0, column=0, padx=5)
    ttk.Button(frame_botoes, text="➕ Adicionar Livro", width=20, command=tela_adicionar_livro).grid(row=0, column=1, padx=5)
    ttk.Button(frame_botoes, text="🚪 Logout", width=20, command=lambda: fazer_logout(janela)).grid(row=0, column=2, padx=5)

    # Consulta o acervo automaticamente ao abrir a janela
    consultar_acervo()


# ===== Tela Principal =====
root = tk.Tk()
root.title("Biblioteca Paulo Freire")
centralizar_janela(root, 400, 300)

# Estilo global (Tema nativo do SO)
style = ttk.Style(root)
if "clam" in style.theme_names():
    style.theme_use("clam")

# Componentes da tela principal
frame_principal = ttk.Frame(root, padding=20)
frame_principal.pack(expand=True, fill="both")

lbl_logo = ttk.Label(frame_principal, text="📚", font=("Arial", 40))
lbl_logo.pack(pady=(10, 0))

ttk.Label(frame_principal, text="Biblioteca Paulo Freire", font=("Arial", 18, "bold")).pack(pady=10)

ttk.Button(frame_principal, text="Entrar no Sistema", width=25, command=abrir_menu_funcionario).pack(pady=10)
ttk.Button(frame_principal, text="Encerrar Programa", width=25, command=root.quit).pack(pady=5)

root.mainloop()