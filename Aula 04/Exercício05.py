# Verificar se um elemento está presente na lista com while Crie um programa que receba uma lista de números e um número específico, e verifique se o número está presente na lista usando um loop while.

numeros = []

indice = 0
encontrado = False

quantidade = int(input("Digite quantos números você deseja inserir na sua lista:\n"))
numero_especifico = int(input("Informe um número específico para verificar se ele está presente na lista de números:\n"))

for numero in range(quantidade):
    numero = int(input("Digite o número que deseja adicionar a sua lista:\n"))
    numeros.append(numero)
    
while indice < len(numeros):
    if numeros[indice] == numero_especifico:
        print(f"O número {numero_especifico} está presente na lista.")
        encontrado = True
        break
    
    indice += 1
    
if not encontrado:
    print(f"O número {numero_especifico} não está presente na lista.")