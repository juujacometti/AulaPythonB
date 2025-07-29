# Escreva uma função que receba um número variável de argumentos posicionais e nomeados e retorne a concatenação de todos eles.

def concatenar(*args, **kwargs):
    return kwargs

concatenado = {} # Dicionário vazio para armazenar os dados do usuário

quantidade = int(input("Informe a quantidade de palavras que deseja concatenar: "))

for i in range(quantidade):
