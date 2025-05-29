# 4 - Verificando Números Pares e Ímpares 🧮

# Solicita um número inteiro ao usuário

while True: # Loop para garantir que a entrada é um número inteiro válido
    try:
        numero = int(input("Digite um número inteiro para verificar se é par ou ímpar: "))
        break # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Verifica se o número é par ou ímpar usando o operador de módulo (%)

if numero % 2 == 0:
    # Se o resto da divisão por 2 for 0, o número é par.
    print(f"O número {numero} é PAR.")
else:
    # Caso contrário, o número é ímpar.
    print(f"O número {numero} é ÍMPAR.")