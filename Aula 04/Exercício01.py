# Imprimir todos os elementos de uma lista com for Escreva um programa que receba uma lista de nomes e imprima cada nome usando um loop for.

nomes = []

quantidade = int(input("Informe quantos nomes terá a sua lista: \n"))

for nome in range(quantidade):
    nome = input("Digite o nome:\n")
    nomes.append(nome)

print("Os nomes inseridos na sua lista são:")
for i in nomes:
    print(i)