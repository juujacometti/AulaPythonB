# Calcular a media de uma lista de números:

lista = []

quantidade = int(input("Informe a quantidade de elementos que você deseja que sua lista contenha:\n"))

for numero in range(quantidade):
    numero = int(input("Digite o número que deseja inserir:\n"))
    lista.append(numero)

media = sum(lista) / quantidade

print(f"\nA média dos valores inseridos na sua lista é: {media}")