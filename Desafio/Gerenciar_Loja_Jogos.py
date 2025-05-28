import y as tk

'''Criar um sistema de comando de uma loja de jogos. 
* O programa deve conter pelo menos 6 listas: quais jogos estão disponíveis para venda, preço de cada jogo, quantidade de jogos disponíveis para venda na loja, preço de fábrica dos jogos para aumentar o 
estoque, registro de vendas e registro de compras de estoque.
* Todas as informações de um jogo devem estar no mesmo indice nas listas.
* Crie um menu interativo com as seguintes opções: Registrar venda, compra de estoque, resumo da loja, sair.
* Ao sair, indique que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade. 
'''

def entrar_sistema():
    while True:
        mensagem = tk.Label()
        mensagem.config(janela, text="🕹️ Menu PlayOn 🕹️", font=("Arial", 16, "bold"))

        label = tk.Label(janela, text="🕹️ Menu PlayOn 🕹️", font=("Arial", 16, "bold"))
        label.grid(row=1, column=0, columnspan=2)
        print("\n----- Menu da Loja de Jogos -----")
        print("1. Registrar venda")
        print("2. Registrar compra de estoque")
        print("3. Resumo da loja")
        print("4. Ver valor em caixa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        # if opcao == '1':
        #     registrar_venda()
        # elif opcao == '2':
        #     registrar_compra()
        # elif opcao == '3':
        #     resumo_loja()
        # elif opcao == '4':
        #     ver_valor_caixa()
        # elif opcao == '5':
        #     print("\nCaixa fechado. Encerrando o sistema.")
        #     break
        # else:
        #     print("Opção inválida. Tente novamente.")

# Criação das listas
jogos_disponiveis = ["Forza Horizon 5", "Minecraft", "Stardew Valley", "Call of Duty", "NBA 2k25"]
preco_jogos = [250.00, 100.00, 15.00, 184.00, 70.00]
quantidade_jogos_disponiveis = [20, 20, 20, 20, 20]
preco_fabrica_jogos = [125.00, 50.00, 7.50, 92.00, 35.00]
vendas = []
compras_estoque = []
formas_pagamento = ["debito", "credito", "pix"]
valor_caixa = 0.0

# Iniciando 
# Janela principal
janela = tk.Tk()
janela.title("Loja de jogos")
janela.geometry("1000x500+500+250") # Largura, altura, distância da parte esquerda da tela, distante da parte superior da tela
janela.grid_rowconfigure(0, weight=1)  # Espaço antes do título
janela.grid_rowconfigure(1, weight=1)  # Linha do título
janela.grid_rowconfigure(2, weight=1)  # Linha dos botões
janela.grid_rowconfigure(3, weight=1)  # Espaço depois dos botões
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

label = tk.Label(janela, text="Bem vindo(a) à PlayOn!", font=("Arial", 16, "bold"))
label.grid(row=1, column=0, columnspan=2)

btn_entrar = tk.Button(janela, text="Entrar", width=15, height=2, font=("Arial", 10), command=entrar_sistema)
btn_fechar = tk.Button(janela, text="Fechar", width=15, height=2, font=("Arial", 10),command=janela.destroy)

btn_entrar.grid(row=2, column=0, pady=10)
btn_fechar.grid(row=2, column=1, pady=10)

janela.mainloop()
    
    