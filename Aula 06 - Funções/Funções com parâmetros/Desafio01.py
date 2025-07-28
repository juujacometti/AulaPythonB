'''
Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de Fibonacci em uma lista.
    * N é definido pelo usuário
Ao encontrar os termos, imprimir a lista e finalizar a função.
'''

def fibonacci(n):
    # Se N for 0 ou 1 retorna ele mesmo direto.
    if n <= 1:
        return n
    # Se for maior, a função vai se chamar e calcular os dois números anteriores e somar eles.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

lista_termos = []

def gerar_lista(n, lista_termos, indice=0):
    # Verificar se todos os termos já foram colocados na lista.
    if indice == n:
        print(lista_termos)
        return

    # Chama a função para calcular o próximo termo e armazena na lista.
    lista_termos.append(fibonacci(indice))
    # Chama ela mesma com N sendo igual, lista atualizada e o índice + 1 para ir para o próximo termo.
    gerar_lista(n, lista_termos, indice + 1)

n = int(input("Digite o número de termos da sequência Fibonacci que você deseja: "))

gerar_lista(n, lista_termos)