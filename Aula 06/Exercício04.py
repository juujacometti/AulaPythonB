# Escreva uma função chamada "imprimir_triângulo" que imprime um triângulo formado por asteriscos

def imprimir_triangulo(linhas):
    for i in range(1, linhas + 1):
        print("*" * i)

linhas = int(input("Informe o número de linhas que o seu triângulo deve conter: "))

imprimir_triangulo(linhas)