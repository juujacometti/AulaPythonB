# Crie uma função que receba uma lista como parâmetro e retorne o maior elemento da lista

def maior_elemento(lista):
    maior = max(lista)
    return maior

lista = [5, 25, 87, 56, 12, 66, 88, 6, 1]

print(f"Lista: {lista}\nO maior elemento presente é: {maior_elemento(lista)}")