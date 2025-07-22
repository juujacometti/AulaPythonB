# Verifique entre dois valores, quais valores são primos
inicio = int(input("Digite o valor inicial:\n"))
fim = int(input("Digite o valor final:\n"))

print(f"Números primos entre {inicio} e {fim}:")

for numero in range(inicio, fim + 1):
    if numero > 1:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                break
        else:
            print(numero)