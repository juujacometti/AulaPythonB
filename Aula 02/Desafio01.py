# Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário

lista = []

numero = int(input("Digite um número inteiro:\n"))

for i in range(1, numero + 1):
    if numero % i == 0:
        lista.append(i)

soma = sum(lista)
print(f"A soma dos divisores do número {numero} é: {soma}")
