'''
Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh, LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH).
Crie uma função que receba os 6 corredores em ordem do vencedor até o último (pedir ao usuário), sendo os três primeiros em
variáveis obrigatórias e os três últimos em kwargs, com as chaves sendo as posições na corrida.
Pedir ao usuário se houve trapaça:
    - se não houve: apresentar a classificação final.
    - se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois, trocá-los de posições.
Por fim, apresentar a classificação final.
'''

def ordem_corredores(primeiro, segundo, terceiro, **kwargs):
    print("\n------------------")
    print(f"=== RESULTADO 🥁 \n\n1º lugar: {primeiro} 🥇\n2º lugar: {segundo} 🥈\n3º lugar: {terceiro} 🥉")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
    print("------------------\n")
    return

print("=== CORRIDA ‍🏃‍➡️ ️\nParticipantes:\n1 - Mercúrio (MC)\n2 - Papa-Léguas (PL)\n3 - Sonic (SN)\n4 - Flash (FS)\n5 - Ligeirinho (LG)\n6 - Super Homem (SH)\n")

primeiro = input("Informe quem ficou em 1º lugar: ")
segundo = input("Informe quem ficou em 2º lugar: ")
terceiro = input("Informe quem ficou em 3º lugar: ")
posicoes = {"4º lugar": "", "5º lugar": "", "6º lugar": ""}

contador = 4 # Apenas para indicar as posições para o usuário

# Preenchimento das posições restantes
for posicao in posicoes:
    competidor = input(f"Digite quem ficou em {contador}º lugar: ")
    posicoes[posicao] = competidor
    contador += 1

trapaca = input("\nHouve trapaça? [S/N]: ")

if trapaca.upper().strip() == "N":
    ordem_corredores(primeiro, segundo, terceiro, **posicoes)

elif trapaca.upper().strip() == "S":
    trapaceiro = input("Digite quem trapaceou: ")
    prejudicado = input("Digite quem foi prejudicado: ")
    classificacao = [primeiro, segundo, terceiro]

    for pos in ["4º lugar", "5º lugar", "6º lugar"]:
        classificacao.append(posicoes[pos])

    # Verificando se os dois nomes existem e trocando as posições do trapaceiro para o prejudicado
    if trapaceiro in classificacao and prejudicado in classificacao:
        idx_trapaceiro = classificacao.index(trapaceiro)
        idx_prejudicado = classificacao.index(prejudicado)
        classificacao[idx_trapaceiro], classificacao[idx_prejudicado] = classificacao[idx_prejudicado], classificacao[idx_trapaceiro]

    else:
        print("\nUm dos nomes digitados não está na classificação.")
        exit()

    # Posições finais
    novo_primeiro = classificacao[0]
    novo_segundo = classificacao[1]
    novo_terceiro = classificacao[2]

    novas_posicoes = {
        "4º lugar": classificacao[3],
        "5º lugar": classificacao[4],
        "6º lugar": classificacao[5]
    }

    ordem_corredores(novo_primeiro, novo_segundo, novo_terceiro, **novas_posicoes)