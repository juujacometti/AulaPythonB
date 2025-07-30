'''
Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh, LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH).
Crie uma função que receba os 6 corredores em ordem do vencedor até o último (pedir ao usuário), sendo os três primeiros em
variáveis obrigatórias e os três últimos em kwargs, com as chaves sendo as posições na corrida.
Pedir ao usuário se houve trapaça:
    - se não houve: apresentar a classificação final.
    - se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois, trocá-los de posições.
Por fim, apresentar a classificação final.
'''

def ordem_corredores(**kwargs):
    primeiro = input("Informe o primeiro colocado: ")
    segundo = input("Informe o segundo colocado: ")
    terceiro = input("Informe o terceiro colocado: ")

    posicoes = {"quarto": "", "quinto": "", "sexto": ""}

    return

print("=== CORRIDA ‍🏃‍➡️ ️\nParticipantes:\n1 - Mercúrio (MC)\n2 - Papa-Léguas (PL)\n3 - Sonic (SN)\n4 - Flash (FS)\n5 - Ligeirinho (LG)\n6 - Super Homem (SH)\n")

ordem_corredores()