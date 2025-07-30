# Escreva uma função que receba um número variável de argumentos nomeados e retorne a média dos valores.

def media(**kwargs):
    # Lista que guarda apenas os valores númericos
    numeros = [float(valor) for valor in kwargs.values() if valor.isnumeric()] # Transforma as strings em float e verifica todos os valores númericos de kwargs e os adiciona na lista

    if len(numeros) == 0: # Verifica se a lista não está vazia
        print("Nenhum valor numérico foi fornecido.")
        return None

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"A média dos valores é: {media}")
    return media

entradas = {} # Guarda todos os conjuntos de chave: valor

quantidade = int(input("Quantas categorias você deseja inserir? "))

for i in range(quantidade):
    chave = input(f"Digite a categoria {i + 1}: ")
    valor = input(f"Digite o conteúdo de '{chave}': ")
    entradas[chave] = valor # Adiciona cada valor a sua determinada chave

media(**entradas)


# Tentativa inicial
# def media(numeros):
#
#     soma = sum(numeros)
#     media = soma / len(numeros)
#
#     print(media)
#     return media
#
# numeros = []
# entradas = {}
#
# quantidade = int(input("Quantas categorias você deseja inserir? "))
#
# for i in range(quantidade):
#     chave = input(f"Digite a categoria {i + 1}: ")
#     valor = input(f"Digite o conteúdo de '{chave}': ")
#     entradas[chave] = valor
#
#     if valor.isnumeric():
#         numeros.append(float(valor))
#
# print(numeros)
#
# media(numeros, **entradas)








