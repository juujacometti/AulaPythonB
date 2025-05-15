# Encontre o primeiro número da sequência de Fibonacci maior que 100

a = 0
b = 1

i = 0

while True:
    a, b = b, a + b
    i += 1

    if a > 100:
        print(a)
        break