# Crie uma função que receba dois números como parâmetros e retorne a soma deles

def soma(num1, num2):
    soma = num1 + num2
    return soma

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

print(f"\nO resultado da soma dos dois números é: {soma(num1, num2)}")
