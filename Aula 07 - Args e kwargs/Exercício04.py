# Escreva uma função que receba um número variável de argumentos posicionais e retorne o maior deles.

def maior_numero(*args):
    maior = max(lista)
    return maior

lista = []

print("Informe cada valor desejado para realizar a soma.\n * Caso deseje parar de inserir valores, digite 'N'.")

while True: # Repete enquanto o usuário digita Strings numéricas
    numero = input("Digite um número: ")
    if numero.isnumeric(): # Verifica se a String é numérica
        lista.append(int(numero))
    else:
        break # Para quando encontrar uma String não numérica

print(f"O maior número digitado foi: {maior_numero(lista)}") # Informa o maior número que foi adicionado na lista

