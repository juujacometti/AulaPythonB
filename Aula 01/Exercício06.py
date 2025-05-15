# Verificar se o aluno está aprovado, reprovado ou em recuperação

nota1 = float(input("Informe a nota da primeira prova:\n"))
nota2 = float(input("Informe a nota da segunda prova:\n"))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"O aluno está reprovado.\nMédia final: {media}")

elif media < 7:
    print(f"O aluno está de recuperação. Média final: {media}")

elif media <= 10:
    print(f"O aluno está aprovado! Média final: {media}")