# Soma dos elementos de uma lista com for Escreva um programa que receba uma lista de números e retorne a soma de todos os elementos usando um loop for.

numeros = []

quantidade = int(input("Digite quantos números você deseja inserir na sua lista:\n"))

for numero in range(quantidade):
    numero = int(input("Digite o número que você deseja inserir:\n"))
    numeros.append(numero)
    soma = sum(numeros)
    
print(soma)