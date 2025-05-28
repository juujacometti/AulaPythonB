import tkinter as tk

def entrar_sistema():
    for widget in janela.winfo_children():
        widget.destroy()

    # Definição do conteúdo que irá aparecer ao iniciar o sistema
    label_menu = tk.Label(janela, text="🕹  Menu PlayOn  🕹️", font=("Arial", 16, "bold"))
    label_menu.grid(row=0, column=0, columnspan=5, pady=(10, 20))

    # Definição de botões de ação
    btn_registrar_venda = tk.Button(janela, text="Registrar venda", width=15, height=2, font=("Arial", 10))
    btn_compra_estoque = tk.Button(janela, text="Compra de estoque", width=15, height=2, font=("Arial", 10))
    btn_jogos_disponiveis = tk.Button(janela, text="Jogos disponíveis", width=15, height=2, font=("Arial", 10))
    btn_resumo_loja = tk.Button(janela, text="Resumo da loja", width=15, height=2, font=("Arial", 10))
    btn_sair = tk.Button(janela, text="Sair", width=15, height=2, font=("Arial", 10), command=janela.destroy)

    btn_registrar_venda.grid(row=1, column=1, pady=5, padx=5)
    btn_compra_estoque.grid(row=1, column=3, pady=5, padx=5)
    btn_jogos_disponiveis.grid(row=2, column=0, pady=5, padx=5)
    btn_resumo_loja.grid(row=2, column=2, pady=5, padx=5)
    btn_sair.grid(row=2, column=5, pady=5, padx=5)


janela = tk.Tk()
janela.title("Loja de jogos")
janela.geometry("1000x500+500+250") # Largura, altura, distância da parte esquerda da tela, distante da parte superior da tela
for i in range(5):
    janela.grid_columnconfigure(i, weight=1)  # 5 colunas
for i in range(4):
    janela.grid_rowconfigure(i, weight=1)

