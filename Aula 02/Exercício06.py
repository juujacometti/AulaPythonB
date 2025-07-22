# Crie uma lista com o quadrado de cada número em outra lista

lista = []
quadrado = []

quantidade = int(input("Informe a quantidade de elementos que você deseja que sua lista contenha:\n"))

for _ in range(quantidade):
    numero = int(input("Informe o número que você deseja adicionar:\n"))
    lista.append(numero)
    quadrado.append(numero * numero)

print(f"\nEsses são os números que você adicionou à sua lista:\n{lista}")
print(f"Esses são os números da sua lista ao quadrado:\n{quadrado}")