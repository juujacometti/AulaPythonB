# Multiplicação de todos os elementos de uma lista com for Escreva um programa que receba uma lista de números e retorne o resultado da multiplicação de todos os elementos usando um loop for.

numeros = []
produto = 1

quantidade = int(input("Digite quantos números você deseja inserir na sua lista:\n"))

for numero in range(quantidade):
    numero = int(input("Digite o número que você deseja inserir:\n"))
    numeros.append(numero)
    
for i in numeros:
    produto *= i

print(f"A multiplicação de todos os elementos que estão dentro da lista é: {produto}")