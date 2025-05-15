# Calcular o fatorial de um número

numero = int(input("Digite um número:\n"))
fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1

print(f"O fatorial é = {fatorial}")