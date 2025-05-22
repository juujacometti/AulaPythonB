'''Crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra para os preços dos produtos. 
Utilizando um loop, preencha as listas com 5 produtos e 5 preços, recebendo estes dados do usuário (input). 
Por fim, some os preços, imprima o valor total e os produtos do carrinho.'''
    
carrinho = []
precos = []

for i in range(1, 6):
    produto = input(f"Digite o nome do produto {i}:\n")
    
    if produto.isalpha():
        carrinho.append(produto)
        
    else:
        print("Isso não é um produto válido.")
        break
    
    
    valor = float(input(f"Informe o preço do produto {i}:\n"))
    precos.append(valor)
    
    valor_total = sum(precos)
    
print(f"Os produtos contidos no seu carrinho são: {carrinho}\nO valor total dos produtos: R${valor_total}")