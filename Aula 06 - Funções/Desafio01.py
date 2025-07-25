'''
Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes, incluindo:
- Nome, sexo, esporte favorito (natação, futebol, vôlei e tênis) e idade.
Com esses dados faça:
    * Função que armazene os dados em uma lista. Dica: use dicionários dentro de uma lista.
    * Calcule a idade média de homens que gostam de natação.
    * Caso não haja homens que gostam de natação, chame uma função e imprima um aviso de que não há homens que gostam de natação.
'''

# Armazena os dados dos habitantes
def armazenar_dados():
    habitantes = []
    habitante1 = {"nome": "Ana", "sexo": "F", "esporte favorito": "Vôlei", "idade": 15}
    habitante2 = {"nome": "João", "sexo": "M", "esporte favorito": "Futebol", "idade": 12}
    habitante3 = {"nome": "Henrique", "sexo": "M", "esporte favorito": "Natação", "idade": 16}
    habitante4 = {"nome": "Jaque", "sexo": "F", "esporte favorito": "Tênis", "idade": 13}

    # Adição dos dicionários à lista
    habitantes.append(habitante1)
    habitantes.append(habitante2)
    habitantes.append(habitante3)
    habitantes.append(habitante4)

    return habitantes

# Calcula a média da idade dos homens que gostam de natação
def media_idade_homens_natacao(habitantes):
    idades_homens_natacao = []

    for habitante in habitantes:
        sexo = habitante["sexo"]
        esporte = habitante["esporte favorito"]
        idade = habitante["idade"]

        if sexo == "M" and esporte == "Natação":
            idades_homens_natacao.append(idade)

    if not idades_homens_natacao: # Verifica se a lista está vazia
        aviso()

    else:
        soma_idades = sum(idades_homens_natacao)
        media = soma_idades / len(idades_homens_natacao)
        print(f"\nA média das idades dos homens que gostam de natação é: {media}")

# Aviso para caso não existam homens que gostam de natação
def aviso():
    print("\nNão há homens que gostam de natação!")

habitantes = armazenar_dados() # Armazena o retorno da lista na variável para que o resultado não se perca

for habitante in habitantes: # Usado para imprimir todos os dicionários
    print(habitante)

media_idade_homens_natacao(habitantes)

