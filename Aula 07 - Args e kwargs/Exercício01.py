# Escreva uma função que receba um número variável de argumentos posicionais e retorne a soma de todos eles.

def somar(*args):
    # Criação da variável que acumulará a soma dos números
    resultado = 0

    # O looping for percorrerá cada valor passado como um argumento, iterando valor sobre valor
    for num in args:
        resultado += num # Atribui o valor de 'num' a variável resultado

    return resultado

lista = [] # Criação de lista para armazenar os valores

print("Informe cada valor desejado para realizar a soma.\n * Caso deseje parar de inserir valores, digite 'N'.")

while True: # Repete enquanto o usuário digita Strings numéricas
    numero = input("Digite o valor para ser calculado: ")
    if numero.isnumeric(): # Verifica se a String é numérica
        lista.append(int(numero))
    else:
        break # Para quando encontrar uma String não numérica

print(somar(*lista)) # Desempacota a lista e roda a função somar() com os seus argumentos

