# Tipos de Triângulos.

lado1 = int(input("Digite o 1º lado: "))
lado2 = int(input("Digite o 2º lado: "))
lado3 = int(input("Digite o 3º lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo: Equilátero")

    elif (lado1 == lado2 != lado3) or (lado3 == lado2 != lado1) or (lado1 == lado3 != lado2):
        print("Triângulo: Isósceles")

    else:
        print("Triângulo: Escaleno")
else:
    print("Os comprimentos informados não formam um triângulo.")