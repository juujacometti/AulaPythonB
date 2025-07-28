'''
Criar 5 funções: uma para um cadastro, outra para realizar o login, outra para mudar a senha,
outra para realizar logout e ainda uma para definir qual opção o usuário deseja escolher.
Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a opção 'sair').
Atente-se às regras:
    - Só é possível realizar um cadastro se não houver nenhum anterior.
    - Só é possível realizar login se houver um cadastro.
    - Só é possível realizar login se o usuário informar corretamente username e senha.
    - Só é possível alterar a senha se o usuário estiver logado.
    - Só é possível alterar a senha se o usuário informar corretamente a senha atual.
    - Só é possível realizar logout se o usuário estiver logado.
'''

usuario = None
senha = None
logado = False

def cadastrar():
    global usuario, senha
    print("===== CADASTRO =====\n")
    if usuario is None:
        usuario = str(input("Digite o nome de usuário: "))
        senha = str(input(f"Digite a senha do {usuario}: "))
        print(f"\nUsuário '{usuario}' cadastrado com sucesso!")
    else:
        print(f"\nUsuário '{usuario}' já cadastrado!")

def login():
    global usuario, senha, logado
    if usuario is not None:
        print("===== LOGIN =====\n")
        usuario_digitado = str(input("Digite o nome do usuário: "))
        if usuario_digitado.strip() == usuario: # Função strip() remove os espaços em branco do início e do fim
            senha_digitada = str(input(f"Digite a senha de {usuario}: "))
            if senha_digitada.strip() == senha:
                print("\nLogin realizado com sucesso!")
                logado = True
            else:
                print(f"\nSenha de {usuario} incorreta!")
        else:
            print(f"\n{usuario_digitado} não está cadastrado!")
    else:
        print("\nNão há nenhuma conta cadastrada no sistema!\n")

def mudar_senha():
    global usuario, senha, logado
    print("===== ALTERAR SENHA =====\n")
    if logado == True:
        while True:
            senha_digitada = str(input("Digite a senha atual: "))
            if senha_digitada.strip() == senha:
                senha_nova = str(input("Digite a nova senha: "))
                senha = senha_nova
                print("\nSenha alterada com sucesso!")
                break
            else:
                print("\nSenha digitada está incorreta!\n")
    else:
        print("É preciso estar logado para alterar senha!")

def logout():
    global usuario, senha, logado
    print("===== DESEJA SAIR? =====\n")
    if logado == True:
        while True:
            confirmar = str(input("Tem certeza que deseja realizar logout? [SIM / NÃO]: "))
            if confirmar.lower().strip() == "sim":
                logado = False
                print("\nEncerramento da conta realizado com sucesso!")
                break
            elif confirmar.lower().strip() == "não" or confirmar.lower().strip() == "nao":
                print("\nCancelando logout...")
                break
            else:
                print("\nDigite 'SIM' ou 'NÃO'!")
    else:
        print("\nÉ preciso estar logado para realizar saída de conta!")

def excluir_conta():
    global usuario, senha, logado
    if logado == True:
        print("===== DESEJA EXCLUIR CONTA? =====\n")
        while True:
            confirmar = str(input("Digite 'SIM' se tem certeza ou 'NÃO' para cancelar: "))
            if confirmar.lower().strip() == 'sim':
                usuario = None
                senha = None
                logado = False
                print("\nExclusão de conta realizada com sucesso!")
                break
            elif confirmar.lower().strip() == 'não' or confirmar.lower().strip() == 'nao':
                print("\nExclusão de conta cancelada com sucesso!")
                break
            else:
                print("\nDigite 'SIM' ou 'NÃO'!")
    else:
        print("É preciso estar logado para realizar exclusão de conta!")

def sair():
    while True:
        sair_sistema = str(input("\nTem certeza que deseja sair do sistema? [SIM / NÃO]: "))
        if sair_sistema.lower().strip() == "nao" or sair_sistema.lower().strip() == "não":
            print("\nCancelando saída do sistema...\n")
            break
        elif sair_sistema.lower().strip() == "sim":
            print("\nSaindo...")
            exit() # Finalizar sistema
        else:
            print("\nDigite 'SIM' ou 'NÃO'!")

def menu():
    while True:
        print("==== MENU =====")
        print("Seja bem vindo(a)!\n\nOpções Disponíveis:\n1 - Cadastro\n2 - Login\n3 - Alterar Senha\n4 - Sair da Conta\n5 - Excluir Conta\n6 - Sair do Sistema\n")
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            login()
        elif opcao == 3:
            mudar_senha()
        elif opcao == 4:
            logout()
        elif opcao == 5:
            excluir_conta()
        elif opcao == 6:
            sair()
        else:
            print("\nDigite uma opção válida!\n")

menu()