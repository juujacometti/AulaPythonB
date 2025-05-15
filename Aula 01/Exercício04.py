# Verificar a faixa etária de uma pessoa

idade = int(input("Informe a sua idade:\n"))

if idade < 0:
    print("Idade inválida")

elif idade <= 12:
    print("Faixa etária: Infantil")

elif idade <= 17:
    print("Faixa etária: Adolescente")

elif idade <= 64:
    print("Faixa etária: Adulto")

elif idade >= 65:
    print("Faixa etária: Idoso")