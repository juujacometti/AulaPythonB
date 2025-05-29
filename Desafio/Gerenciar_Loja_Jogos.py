import tkinter as tk
from tkinter import messagebox # Pop up de confirmação/erro

'''Criar um sistema de comando de uma loja de jogos. 
* O programa deve conter pelo menos 6 listas: quais jogos estão disponíveis para venda, preço de cada jogo, quantidade de jogos disponíveis para venda na loja, preço de fábrica dos jogos para aumentar o 
estoque, registro de vendas e registro de compras de estoque.
* Todas as informações de um jogo devem estar no mesmo indice nas listas.
* Crie um menu interativo com as seguintes opções: Registrar venda, compra de estoque, resumo da loja, sair.
* Ao sair, indique que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade. 
'''

# Criação das listas
jogos_disponiveis = ["Forza Horizon 5", "Minecraft", "Stardew Valley", "Call of Duty", "NBA 2k25"]
preco_jogos = [250.00, 100.00, 15.00, 184.00, 70.00]
quantidade_jogos_disponiveis = [20, 20, 20, 20, 20]
preco_fabrica_jogos = [125.00, 50.00, 7.50, 92.00, 35.00]
vendas = []
compras_estoque = []
valor_caixa = 0.0

# Funções 
def registrar_venda():
    janela_venda = tk.Toplevel()
    janela_venda.title("Registrar venda")

    tk.Label(janela_venda, text="Selecione o jogo vendido:").pack(pady=10)

    for i in range(len(jogos_disponiveis)):
        frame = tk.Frame(janela_venda)
        frame.pack(pady=5)

        texto = f"{jogos_disponiveis[i]} - R${preco_jogos[i]:.2f} - Estoque: {quantidade_jogos_disponiveis[i]}"
        tk.Label(frame, text=texto).grid(row=0, column=0, padx=5)

        tk.Label(frame, text="Qtd:").grid(row=0, column=1)
        quantidade_entry = tk.Entry(frame, width=5)
        quantidade_entry.grid(row=0, column=2, padx=5)

        botao = tk.Button(frame, text="Vender",
                          command=lambda i=i, q=quantidade_entry: efetuar_venda(i, janela_venda, q))
        botao.grid(row=0, column=3, padx=5)

# Função criada para contabilizar a quantidade de produtos inserida pelo usuário da função realizar_venda 
def efetuar_venda(index, janela_venda, quantidade_entry):
    global valor_caixa  # Atualizar o valor do caixa

    try:
        quantidade = int(quantidade_entry.get())
        if quantidade <= 0:
            messagebox.showerror("Erro", "Quantidade inválida.") # Erro para caso a quantidade informada seja menot que zero
            return
        if quantidade > quantidade_jogos_disponiveis[index]:
            messagebox.showerror("Erro", "Estoque insuficiente.") # Erro para caso a quantidade informada não possua estoque suficiete
            return

        total = quantidade * preco_jogos[index]
        quantidade_jogos_disponiveis[index] -= quantidade
        vendas.append((jogos_disponiveis[index], quantidade, total))
        valor_caixa += total

        messagebox.showinfo("Sucesso", f"Realizada a venda de {quantidade} unidade(s) de '{jogos_disponiveis[index]}'") 
        janela_venda.destroy()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido.")

def compra_estoque():
    janela_compra = tk.Toplevel()
    janela_compra.title("Abastecer estoque")

    tk.Label(janela_compra, text="Selecione o jogo que deseja comprar:").pack(pady=10)

    for i in range(len(jogos_disponiveis)):
        frame = tk.Frame(janela_compra)
        frame.pack(pady=5)

        texto = f"{jogos_disponiveis[i]} - R${preco_fabrica_jogos[i]:.2f} - Estoque: {quantidade_jogos_disponiveis[i]}"
        tk.Label(frame, text=texto).grid(row=0, column=0, padx=5)

        tk.Label(frame, text="Qtd:").grid(row=0, column=1)
        quantidade_entry = tk.Entry(frame, width=5)
        quantidade_entry.grid(row=0, column=2, padx=5)

        botao = tk.Button(frame, text="Comprar",command=lambda i=i, q=quantidade_entry: efetuar_compra(i, janela_compra, q))
        botao.grid(row=0, column=3, padx=5)
        
def efetuar_compra(index, janela_compra, quantidade_entry):
    global valor_caixa

    try:
        quantidade = int(quantidade_entry.get())
        if quantidade <= 0:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return

        custo_total = quantidade * preco_fabrica_jogos[index]
        if valor_caixa < custo_total:
            messagebox.showerror("Erro", "Saldo insuficiente.")
            return

        quantidade_jogos_disponiveis[index] += quantidade
        valor_caixa -= custo_total
        compras_estoque.append((jogos_disponiveis[index], quantidade, custo_total))

        messagebox.showinfo("Sucesso", f"{quantidade} unidade(s) de '{jogos_disponiveis[index]}' comprada(s)!")
        janela_compra.destroy()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def resumo_playon():
    janela_resumo = tk.Toplevel()
    janela_resumo.title("Resumo - PlayOn")
    
    # Exibe a quantidade disponível em estoque 
    tk.Label(janela_resumo, text="******** ESTOQUE DISPONÍVEL ******** ").pack(pady=5)
    for i in range(len(jogos_disponiveis)):
        texto = f"{jogos_disponiveis[i]} | R${preco_jogos[i]:.2f} | Quantidade: {quantidade_jogos_disponiveis[i]}"
        tk.Label(janela_resumo, text=texto).pack()
        
    # Exibe o valor que foi lucrado com vendas 
    tk.Label(janela_resumo, text="\n******** VENDAS ********").pack(pady=5)
    total_vendas = sum(venda[2] for venda in vendas)  # Soma os valores em reais
    for venda in vendas:
        tk.Label(janela_resumo, text=f"{venda[0]} - {venda[1]}x - R${venda[2]:.2f}").pack()  # Mostra nome, qtd, valor
    tk.Label(janela_resumo, text=f"Ganhos com vendas: R${total_vendas:.2f}").pack()
    
    # Exibe o valor que foi gasto com estoque
    tk.Label(janela_resumo, text="\n******** COMPRAS ********").pack(pady=5)
    total_despesas = sum(compra[2] for compra in compras_estoque)
    for compra in compras_estoque:
        tk.Label(janela_resumo, text=f"{compra[1]}x {compra[0]} - R${compra[2]:.2f}").pack()
    tk.Label(janela_resumo, text=f"Total em compras: R${total_despesas:.2f}").pack()
    
    # Exibe o saldo geral (vendas - compras)
    tk.Label(janela_resumo, text="\n******** SALDO ATUAL ********").pack(pady=5)   
    tk.Label(janela_resumo, text=f"\nR${valor_caixa:.2f}").pack()


# Janela principal
janela_principal = tk.Tk() # Criação de janela inicial
janela_principal.title("Gerenciamento PlayOn") # Título da janela
janela_principal.geometry("800x500+280+150") #Largura, altura, distância da parte esquerda da tela, distante da parte superior da tela

tk.Label(janela_principal, text="Bem vindo(a) à PlayOn!", font=("Arial", 16, "bold")).pack(pady=20) # Titulo janela inicial

frame_menu = tk.Frame(janela_principal) # Para organizar widgets
frame_menu.pack() # Ocupar espaço disponível

# Cria e inserie os bptões na tela
tk.Button(frame_menu, text="Registrar Venda", width=20, height=2, command=registrar_venda).grid(row=0, column=0, padx=10, pady=10) 
tk.Button(frame_menu, text="Compra de Estoque", width=20, height=2, command=compra_estoque).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_menu, text="Resumo da Loja", width=20, height=2, command=resumo_playon).grid(row=1, column=0, padx=10, pady=10)
tk.Button(frame_menu, text="Sair", width=20, height=2, command=janela_principal.destroy).grid(row=1, column=1, padx=10, pady=10)

janela_principal.mainloop() # Inicia a janela