# Listas principais
jogos_disponiveis = ["Forza Horizon 5", "Minecraft", "Stardew Valley", "Call of Duty", "NBA 2k25"]
preco_jogos = [250.00, 100.00, 15.00, 184.00, 70.00]
quantidade_jogos_disponiveis = [20, 20, 20, 20, 20]
preco_fabrica_jogos = [125.00, 50.00, 7.50, 92.00, 35.00]
vendas = []
compras_estoque = []
formas_pagamento = ["débito", "crédito", "pix"]
valor_caixa = [0.0]


def exibir_jogos():
    print("\nJogos disponíveis:")
    for i, jogo in enumerate(jogos_disponiveis):
        print(f"{i + 1}. {jogo} - R${preco_jogos[i]:.2f} - {quantidade_jogos_disponiveis[i]} unidades")


def registrar_venda():
    exibir_jogos()
    try:
        escolha = int(input("\nDigite o número do jogo vendido: ")) - 1
        if 0 <= escolha < len(jogos_disponiveis):
            if quantidade_jogos_disponiveis[escolha] > 0:
                quantidade = int(input("Quantidade vendida: "))
                if quantidade <= quantidade_jogos_disponiveis[escolha]:
                    print("Formas de pagamento disponíveis: ", ", ".join(formas_pagamento))
                    pagamento = input("Digite a forma de pagamento: ").lower()
                    if pagamento in formas_pagamento:
                        total = preco_jogos[escolha] * quantidade
                        vendas.append((jogos_disponiveis[escolha], quantidade, total, pagamento))
                        quantidade_jogos_disponiveis[escolha] -= quantidade
                        valor_caixa[0] += total
                        print(f"Venda registrada com sucesso. Total: R${total:.2f}")
                    else:
                        print("Forma de pagamento inválida.")
                else:
                    print("Quantidade indisponível em estoque.")
            else:
                print("Jogo fora de estoque.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")


def registrar_compra():
    exibir_jogos()
    try:
        escolha = int(input("\nDigite o número do jogo para comprar estoque: ")) - 1
        if 0 <= escolha < len(jogos_disponiveis):
            quantidade = int(input("Quantidade a ser comprada: "))
            custo = preco_fabrica_jogos[escolha] * quantidade
            print(f"Custo total da compra: R${custo:.2f}")
            confirmacao = input("Deseja confirmar a compra? (s/n): ").lower()
            if confirmacao == 's':
                if custo <= valor_caixa[0]:
                    compras_estoque.append((jogos_disponiveis[escolha], quantidade, custo))
                    quantidade_jogos_disponiveis[escolha] += quantidade
                    valor_caixa[0] -= custo
                    print(f"Compra registrada. Custo: R${custo:.2f}")
                else:
                    print("Saldo insuficiente no caixa.")
            else:
                print("Compra cancelada.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")


def resumo_loja():
    print("\n--- Resumo da Loja ---")
    print(f"Valor em caixa: R${valor_caixa[0]:.2f}")
    print("\nVendas realizadas:")
    if vendas:
        for v in vendas:
            print(f"Jogo: {v[0]} | Quantidade: {v[1]} | Total: R${v[2]:.2f} | Pagamento: {v[3]}")
    else:
        print("Nenhuma venda registrada.")

    print("\nCompras de estoque:")
    if compras_estoque:
        for c in compras_estoque:
            print(f"Jogo: {c[0]} | Quantidade: {c[1]} | Custo: R${c[2]:.2f}")
    else:
        print("Nenhuma compra registrada.")

    print("\nEstoque atual:")
    exibir_jogos()


def ver_valor_caixa():
    print(f"\n💰 Valor atual em caixa: R${valor_caixa[0]:.2f}")


# Loop do menu principal
def menu():
    while True:
        print("\n----- Menu da Loja de Jogos -----")
        print("1. Registrar venda")
        print("2. Registrar compra de estoque")
        print("3. Resumo da loja")
        print("4. Ver valor em caixa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_venda()
        elif opcao == '2':
            registrar_compra()
        elif opcao == '3':
            resumo_loja()
        elif opcao == '4':
            ver_valor_caixa()
        elif opcao == '5':
            print("\nCaixa fechado. Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o sistema
menu()
