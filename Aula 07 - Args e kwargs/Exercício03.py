# Escreva uma função que receba um número variável de argumentos posicionais e nomeados e retorne a concatenação de todos eles.

def concatenar(*args, **kwargs):
    string = "".join(args)

    for chave, valor in kwargs.items():
        string += f"{chave}{valor}"

    print(string)
    return string

entradas = {}
lista = []

print("Se quiser parar digite 'PARAR'")

while True:
    while True:
        p = input("Digite os argumentos posicionais: ")
        if p != 'PARAR':
            lista.append(p)

        elif p == 'PARAR':
            break

    escolha = input("Você deseja inserir argumentos nomeados? (S/N): ")

    if escolha == 'S':
        quantidade = int(input("Quantas categorias você deseja inserir? "))

        for i in range(quantidade):
            chave = input(f"Digite a categoria {i + 1}: ")
            valor = input(f"Digite o conteúdo de {chave}': ")
            entradas[chave] = valor

    break

concatenar(*lista, **entradas)
