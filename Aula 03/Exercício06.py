'''
Faça um programa que calcule o maior palíndromo resultado do produto de dois números de 3 dígitos (são números que lendo da esquerda para a
direita resulta no mesmo número caso leia da direita para a esquerda). Exemplo: o maior palíndromo resultado do produto de dois núemros é
91 * 99 = 9009.
'''

# Inicializando variáveis
maior_palindromo = 0
fatores = (0, 0)
i = 100  # Inicializando i
j = 100  # Inicializando j

# Loop com while
while i < 1000:
    while j < 1000:
        numero = i * j
        numero_string = str(numero)

        # Verifica se o número é palíndromo e maior que o atual maior palíndromo
        if numero_string == numero_string[::-1] and numero > maior_palindromo:
            maior_palindromo = numero
            fatores = (i, j)

        j += 1  # Incrementa j

    i += 1  # Incrementa i
    j = 100  # Reseta j para 100, para que o loop interno seja executado novamente

# Exibe o resultado
print(f"O maior palíndromo é {maior_palindromo} = {fatores[0]} x {fatores[1]}")
