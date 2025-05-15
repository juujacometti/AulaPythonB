# Crie um personagem e defina suas características

cor_cabelo = input("Informe a cor de cabelo do seu personagem:\n")
cor_pele = input("Informe a cor de pele do seu personagem:\n")
classe = input("Informe a classe do seu personagem (guerreiro, mago ou arqueiro):\n")
idade = int(input("Inforne a idade do seu personagem:\n"))
altura = float(input("Inforne a altura do seu personagem:\n"))
habilidade = input("Escolha uma habilidade específica do seu personagem:\n")
nome = input("Informe o nome do seu personagem:\n")

print(f"\nSeu personagem:\nNome: {nome}\nCabelo: {cor_cabelo}\nPele: {cor_pele}\nIdade: {idade}\nAltura: {altura}\nClasse: {classe}\nHabilidade específica: {habilidade}")