# Imprimir os 5 primeiros números pares

numero = 1
lista = []

while len(lista) < 5:
    if numero % 2 == 0:
        lista.append(numero)
    numero += 1

print(lista)

