# Crie uma função que receba uma string e um caractere como parâmetros e retorne o número de vezes que o caractere aparece na string

def quantia_caractere(string, caractere):
    quantidade_caracteres = 0
    for i in string:
        if i == caractere:
            quantidade_caracteres += 1

    return quantidade_caracteres

string = input("Digite uma frase ou palavra: ")
caractere = input("Informe o caractere que você deseja contar na frase/palavra: ")

print(f"A frase/palavra possui {quantia_caractere(string,caractere)} caracteres do tipo '{caractere}'")

