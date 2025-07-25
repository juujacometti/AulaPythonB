# Escreva uma função chamada "mostrar_menu" que imprime um menu simples com algumas opções

def mostrar_menu():
    escolha = int(input(f"{3 * '='} MENU DE OPÇÕES {3 * '='}\n1. Bem-vindo\n2. Adeus\n3. Sair\n"))

    if escolha == 1:
        print("Bem-vindo usuário(a)!")

    elif escolha == 2:
        print("Até mais usuário(a)!")

    elif escolha == 3:
        print("Saindo...")

    else:
        print("Escolha inválida, tente novamente!")

mostrar_menu()


