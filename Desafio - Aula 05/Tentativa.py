import tkinter as tk

'''Criar um sistema de comando de uma loja de jogos. 
* O programa deve conter pelo menos 6 listas: quais jogos estão disponíveis para venda, preço de cada jogo, quantidade de jogos disponíveis para venda na loja, preço de fábrica dos jogos para aumentar o 
estoque, registro de vendas e registro de compras de estoque.
* Todas as informações de um jogo devem estar no mesmo indice nas listas.
* Crie um menu interativo com as seguintes opções: Registrar venda, compra de estoque, resumo da loja, sair.
* Ao sair, indique que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade. 
'''
def entrar_sistema():
    for widget in janela.winfo_children():
        widget.destroy()

    # Definição do conteúdo que irá aparecer ao iniciar o sistema
    label_menu = tk.Label(janela, text="🕹  Menu PlayOn  🕹️", font=("Arial", 16, "bold"))
    label_menu.grid(row=0, column=0, columnspan=5, pady=(10, 20))

    # Definição de botões de ação
    btn_registrar_venda = tk.Button(janela, text="Registrar venda", width=15, height=2, font=("Arial", 10), command=registro_venda)
    btn_compra_estoque = tk.Button(janela, text="Compra de estoque", width=15, height=2, font=("Arial", 10), command=compra_estoque)
    btn_jogos_disponiveis = tk.Button(janela, text="Jogos disponíveis", width=15, height=2, font=("Arial", 10), command=lista_jogos_disponiveis)
    btn_resumo_loja = tk.Button(janela, text="Resumo da loja", width=15, height=2, font=("Arial", 10))
    btn_sair = tk.Button(janela, text="Sair", width=15, height=2, font=("Arial", 10), command=janela.destroy)

    btn_registrar_venda.grid(row=1, column=1, pady=5, padx=5)
    btn_compra_estoque.grid(row=1, column=3, pady=5, padx=5)
    btn_jogos_disponiveis.grid(row=2, column=0, pady=5, padx=5)
    btn_resumo_loja.grid(row=2, column=2, pady=5, padx=5)
    btn_sair.grid(row=2, column=5, pady=5, padx=5)

def registro_venda():
    for widget in janela.winfo_children():
        widget.destroy()

    # Definição de conteúdo de registro de venda
    label_venda = tk.Label(janela, text="Você deseja realizar o registro de venda de qual jogo?", font=("Arial", 16, "bold"))
    label_venda.grid(row=0, column=0, columnspan=5, pady=(10, 20))

    btn_vende_Forza = tk.Button(janela, text="Forza Horizon 5", width=15, height=2, font=("Arial", 10), command=lambda: abrir_campo_quantidade("Forza Horizon 5"))
    btn_vende_Minecraft = tk.Button(janela, text="Minecraft", width=15, height=2, font=("Arial", 10), command=lambda: abrir_campo_quantidade("Minecraft"))
    btn_vende_Stardew = tk.Button(janela, text="Stardew Valley", width=15, height=2, font=("Arial", 10), command=lambda: abrir_campo_quantidade("Stardew Valley"))
    btn_vende_Cod = tk.Button(janela, text="Call of Duty", width=15, height=2, font=("Arial", 10), command=lambda: abrir_campo_quantidade("Call of Duty"))
    btn_vende_Nba = tk.Button(janela, text="NBA 2k25", width=15, height=2, font=("Arial", 10), command=lambda: abrir_campo_quantidade("NBA 2k25"))

    btn_vende_Forza.grid(row=1, column=1, pady=5, padx=5)
    btn_vende_Minecraft.grid(row=1, column=3, pady=5, padx=5)
    btn_vende_Stardew.grid(row=2, column=0, pady=5, padx=5)
    btn_vende_Cod.grid(row=2, column=2, pady=5, padx=5)
    btn_vende_Nba.grid(row=2, column=5, pady=5, padx=5)

def abrir_campo_quantidade(jogo):
    for widget in janela.winfo_children():
        widget.destroy()

    label_venda_jogo = tk.Label(janela, text=f"Digite a quantidade para o jogo {jogo}:", font=("Arial", 14))
    label_venda_jogo.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

    entrada_quantidade = tk.Entry(janela)
    entrada_quantidade.grid(row=1, column=1, pady=10, padx=10)

    def confirmar():
        quantidade_str = entrada_quantidade.get()
        if quantidade_str.isdigit() and int(quantidade_str) > 0:
            quantidade = int(quantidade_str)
            idx = jogos_disponiveis.index(jogo)

            if quantidade <= quantidade_jogos_disponiveis[idx]:
                valor_venda = quantidade * preco_jogos[idx]
                quantidade_jogos_disponiveis[idx] -= quantidade
                label_registro_venda = tk.Label(janela, text=f"Registrado: Venda de {quantidade} unidades de {jogo}",font=("Arial", 12, "bold"))
                label_registro_venda.grid(row=2, column=1, columnspan=5, pady=(10, 20))
                label_valor_venda = tk.Label(janela, text=(f"Valor da venda: {valor_venda}"), font=("Arial", 12, "bold"))
                label_valor_venda.grid(row=3, column=1, pady=10, padx=10)
        else:
            label_invalido= tk.Label(janela, text=(f"Valor inválido! Tente novamente."), font=("Arial", 12, "bold"))
            label_invalido.grid(row=3, column=1, pady=10, padx=10)

    btn_confirmar = tk.Button(janela, text="Confirmar", command=confirmar)
    btn_confirmar.grid(row=1, column=2, pady=10, padx=10)

def compra_estoque():
    for widget in janela.winfo_children():
        widget.destroy()
    label_compra = tk.Label(janela, text="Qual jogo você deseja comprar para o estoque?", font=("Arial", 12))
    label_compra.grid(row=0, column=0, columnspan=5, pady=(10, 20))

    btn_jogo_Forza = tk.Button(janela, text="Forza Horizon 5", width=15, height=2, font=("Arial", 10), command=lambda: quantidade_compra("Forza Horizon 5"))
    btn_jogo_Minecraft = tk.Button(janela, text="Minecraft", width=15, height=2, font=("Arial", 10), command=lambda: quantidade_compra("Minecraft"))
    btn_jogo_Stardew = tk.Button(janela, text="Stardew Valley", width=15, height=2, font=("Arial", 10), command=lambda: quantidade_compra("Stardew Valley"))
    btn_jogo_Cod = tk.Button(janela, text="Call of Duty", width=15, height=2, font=("Arial", 10), command=lambda: quantidade_compra("Call of Duty"))
    btn_jogo_Nba = tk.Button(janela, text="NBA 2k25", width=15, height=2, font=("Arial", 10), command=lambda: quantidade_compra("NBA 2k25"))

    btn_jogo_Forza.grid(row=1, column=1, pady=5, padx=5)
    btn_jogo_Minecraft.grid(row=1, column=3, pady=5, padx=5)
    btn_jogo_Stardew.grid(row=2, column=0, pady=5, padx=5)
    btn_jogo_Cod.grid(row=2, column=2, pady=5, padx=5)
    btn_jogo_Nba.grid(row=2, column=5, pady=5, padx=5)

def quantidade_compra(jogo):
    for widget in janela.winfo_children():
        widget.destroy()

    label_compra_estoque = tk.Label(janela, text=f"Digite a quantidade para o jogo {jogo}:", font=("Arial", 14))
    label_compra_estoque.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

    entrada_quantidade = tk.Entry(janela)
    entrada_quantidade.grid(row=1, column=1, pady=10, padx=10)

    def confirmar():
        quantidade_str = entrada_quantidade.get()
        if quantidade_str.isdigit() and int(quantidade_str) > 0:
            quantidade = int(quantidade_str)
            idx = jogos_disponiveis.index(jogo)

            if quantidade <= quantidade_jogos_disponiveis[idx]:
                valor_compra = quantidade * preco_fabrica_jogos[idx]
                quantidade_jogos_disponiveis[idx] += quantidade
                label_registro_compra = tk.Label(janela, text=f"Registrado: Compra de {quantidade} unidades do {jogo}",font=("Arial", 12, "bold"))
                label_registro_compra.grid(row=2, column=1, columnspan=5, pady=(10, 20))
                label_valor_venda = tk.Label(janela, text=(f"Valor da compra: {valor_compra}"), font=("Arial", 12, "bold"))
                label_valor_venda.grid(row=3, column=1, pady=10, padx=10)
        else:
            label_invalido= tk.Label(janela, text=(f"Valor inválido! Tente novamente."), font=("Arial", 12, "bold"))
            label_invalido.grid(row=3, column=1, pady=10, padx=10)

    btn_confirmar = tk.Button(janela, text="Confirmar", command=confirmar)
    btn_confirmar.grid(row=1, column=2, pady=10, padx=10)

def lista_jogos_disponiveis():
    for widget in janela.winfo_children():
        widget.destroy()

    label_disponivel_forza = tk.Label(janela, text="Forza Horizon 5", font=("Arial", 12))
    label_disponivel_forza.grid(row=0, column=1)
    label_disponivel_minecraft = tk.Label(janela, text="Minecraft", font=("Arial", 12))
    label_disponivel_minecraft.grid(row=1, column=1)
    label_disponivel_stardew = tk.Label(janela, text="Stardew Valley", font=("Arial", 12))
    label_disponivel_stardew.grid(row=2, column=1)
    label_disponivel_cod = tk.Label(janela, text="Call of Duty", font=("Arial", 12))
    label_disponivel_cod.grid(row=3, column=1)
    label_disponivel_nba = tk.Label(janela, text="NBA 2k25", font=("Arial", 12))
    label_disponivel_nba.grid(row=4, column=1)

def resumo_loja():
    label_resumo_loja = tk.Label(janela, text="Resumo da loja", font=("Arial", 14, "bold"))
    label_resumo_loja.grid(row=0, column=1, padx=10)

    label_valor_caixa = tk.Label(janela, text=(f"Valor em caixa: {valor_caixa}" ), font=("Arial", 12))
    label_valor_caixa.grid(row=1, column=1, padx=10)


# Criação das listas
jogos_disponiveis = ["Forza Horizon 5", "Minecraft", "Stardew Valley", "Call of Duty", "NBA 2k25"]
preco_jogos = [250.00, 100.00, 15.00, 184.00, 70.00]
quantidade_jogos_disponiveis = [20, 20, 20, 20, 20]
preco_fabrica_jogos = [125.00, 50.00, 7.50, 92.00, 35.00]
vendas = []
compras_estoque = []
formas_pagamento = ["debito", "credito", "pix"]
valor_caixa = 0.0

# Janela principal
janela = tk.Tk()
janela.title("Loja de jogos")
janela.geometry("1000x500+500+250") # Largura, altura, distância da parte esquerda da tela, distante da parte superior da tela
for i in range(5):
    janela.grid_columnconfigure(i, weight=1)  # 5 colunas
for i in range(4):
    janela.grid_rowconfigure(i, weight=1)

label = tk.Label(janela, text="Bem vindo(a) à PlayOn!", font=("Arial", 16, "bold"))
label.grid(row=0, column=1, columnspan=3)

btn_entrar = tk.Button(janela, text="Entrar", width=15, height=2, font=("Arial", 10), command=entrar_sistema)
btn_fechar = tk.Button(janela, text="Fechar", width=15, height=2, font=("Arial", 10),command=janela.destroy)

btn_entrar.grid(row=1, column=1, pady=10)
btn_fechar.grid(row=1, column=2, pady=10)

janela.mainloop()