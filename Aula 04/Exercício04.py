# Contagem de vogais em uma lista de palavras. Crie um programa que receba uma lista de palavras e retorne a quantidade total de vogais em todas as palavras usando um loop.

palavras = []

vogais = 0

quantidade = int(input("Informe a quantidade de palavras que a sua lista terá:\n"))

for palavra in range(quantidade):
    palavra = input("Digite a palavra que você deseja incluir na sua lista:\n")
    palavras.append(palavra)
    

print(f"\nNa lista \n  {palavras}\nexistem:")

for palavra in palavras:
    for letra in palavra:  # Itera sobre cada letra da palavra
        if letra.lower() in "aeiou":  # Verifica se a letra é uma vogal
            vogais += 1
        
print(f"Vogais: {vogais}")