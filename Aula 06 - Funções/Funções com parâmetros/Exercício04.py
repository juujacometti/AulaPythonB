# Crie uma função que receba uma lista de números como parâmetro e retorne a média aritmética dos elementos

def media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

lista = [5, 13, 28, 26]

print(f"Lista de elementos: {lista}\nA média aritimética desses elementos é: {media(lista)}")