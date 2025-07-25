# Crie uma função chamada "mostrar_hora" que imprime a hora atual do sistema

from datetime import datetime # Módeulo da biblioteca padrão usado para data e hora

def mostrar_hora():
    hora_atual = datetime.now().strftime("%H:%M:%S") # Função now retorna a hora atual do sistema
    print("Hora atual:", hora_atual)

# Exemplo de uso
mostrar_hora()