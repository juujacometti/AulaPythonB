# Crie uma função que receba uma lista de palavras como parâmetro e retorne a quantidade de palavras que começam com a letra "a"

def palavras_inicio_a(lista):
    quantidade = 0
    for i in lista:
        if i[0] == "a" or i[0] == "A":
            quantidade += 1
    return quantidade

lista = ["aula", "alunos", "mouse", "fone de ouvido", "computador", "Apoio de mão"]

print(f"Lista de palavras: {lista}\nDentro dessa lista, {palavras_inicio_a(lista)} palavras começam com a letra 'A'")