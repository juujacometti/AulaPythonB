'''
Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes, incluindo:
- Nome, sexo, esporte favorito (natação, futebol, vôlei e tênis) e idade.
Com esses dados faça:
    * Função que armazene os dados em uma lista. Dica: use dicionários dentro de uma lista.
    * Calcule a idade média de homens que gostam de natação.
    * Caso não haja homens que gostam de natação, chame uma função e imprima um aviso de que não há homens que gostam de natação.
Adição de inputs ao desafio.
'''

# Armazena os dados dos habitantes
def armazenar_dados():
    habitantes = []

    for i in range(4):
        print(f"=== Habitante {i + 1} ===")
        nome = input("Digite o nome: ")
        sexo = input("Informe o sexo (F/M): ")
        esporte_favorito = input("Informe qual desses esportes é o favortito (natação, futebol, vôlei e tênis): ")
        idade = int(input("Informe a idade: "))

        habitante = {"nome": nome, "sexo": sexo, "esporte favorito": esporte_favorito, "idade": idade}

        # Adição dos dicionários à lista
        habitantes.append(habitante)

    return habitantes

# Calcula a média da idade dos homens que gostam de natação
def media_idade_homens_natacao(habitantes):
    idades_homens_natacao = []

    for habitante in habitantes:
        sexo = habitante["sexo"]
        esporte = habitante["esporte favorito"]
        idade = habitante["idade"]

        if sexo == "M" and esporte == "natação":
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