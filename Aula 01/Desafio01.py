# Verificar se um número é primo

numero = int(input("Digite um número inteiro:\n"))

# Lopping para verificar entre os dois números, quais valores são primos
if numero <= 1:
    print(f"O número {numero} não é primo.")

else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"\nO número {numero} não é primo.")
            break

    else:
        print(f"\nO número {numero} é primo.")