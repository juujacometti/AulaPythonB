import tkinter as tk

'''Criar um sistema de comando de uma loja de jogos. 
* O programa deve conter pelo menos 6 listas: quais jogos estão disponíveis para venda, preço de cada jogo, quantidade de jogos disponíveis para venda na loja, preço de fábrica dos jogos para aumentar o 
estoque, registro de vendas e registro de compras de estoque.
* Todas as informações de um jogo devem estar no mesmo indice nas listas.
* Crie um menu interativo com as seguintes opções: Registrar venda, compra de estoque, resumo da loja, sair.
* Ao sair, indique que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade. 
'''

# Criação das listas
jogos_disponiveis = ["Forza Horizon 5", "Minecrft", "Stardew Valley", "Call of Duty", "NBA 2k25"]
preco_jogos = [250.00, 100.00, 15.00, 184.00, 70.00]
quantidade_jogos_disponiveis = [20, 20, 20, 20, 20]
preco_fabrica_jogos = [125.00, 50.00, 7.50, 92.00, 35.00]
vendas = []
compras_estoque = []
formas_pagamento = ["debito", "credito", "pix"]
valor_caixa = []

# Iniciando 
# Janela principal
janela = tk.Tk()
janela.title("Loja de jogos")
janela.geometry("1000x500")

label = tk.Label(janela, text= "Bem vindo(a) à PlayOn!")
label.pack()

btn_entrar = tk.Button(janela, text="Entrar", command=entrar_sistema())
btn_entrar.pack()

btn_fechar = tk.Button(janela, text="Fechar")
btn_fechar.pack()

janela.mainloop()
    
    