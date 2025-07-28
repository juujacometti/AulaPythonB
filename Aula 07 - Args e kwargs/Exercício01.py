# Escreva uma função que receba um número variável de argumentos posicionais e retorne a soma de todos eles.

def somar(*args):
    # Criação da variável que acumulará a soma dos números
    resultado = 0
    # O looping for percorrerá cada valor passado como um argumento, iterando valor sobre valor
    for num in args:
        resultado += num # Atribui o valor de 'num' a variável resultado
        return resultado

