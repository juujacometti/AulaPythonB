# Escreva uma função que receba um número variável de argumentos nomeados e retorne um dicionário com esses argumentos.

def criar_dicionario(**kwargs): # Dentro dessa função, kwargs é considerado dicionário
    return kwargs # Kwargs será um dicionário com os argumentos passados

entradas = {} # Dicionário vazio para armazenar os dados

# Quantos pares chave-valor o usuário deseja inserir
quantidade = int(input("Quantas categorias você deseja inserir? "))

for i in range(quantidade): 
    chave = input(f"Digite a categoria {i+1}: ") # {i + 1} -> serve apenas para mostrar o número da categoria (chave) atual
    valor = input(f"Digite o conteúdo de {chave}': ") # Solicitação do valor referente àquela chave/categoria
    entradas[chave] = valor  # Adiciona ao dicionário o valor referente a chave específica


print("\nDicionário final:") # Passando o dicionário como 'argumentos nomeados' usando **
print(criar_dicionario(**entradas))