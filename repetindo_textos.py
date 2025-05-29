# Solicita uma string (texto) ao usuário

texto_para_repetir = input("Digite um texto para ser repetido: ")

# Solicita um número inteiro para a quantidade de repetições

while True:
    try:
        quantidade_repeticoes = int(input("Quantas vezes você deseja repetir o texto? (Digite um número inteiro): "))
        if quantidade_repeticoes >= 0: # Garante que o número não é negativo
            break
        else:
            print("Por favor, digite um número inteiro não negativo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")


# Repete a string o número de vezes informado
texto_com_espaco = texto_para_repetir + " "
texto_repetido = texto_com_espaco * quantidade_repeticoes

# Exibe o texto repetido

print(f"\nO texto repetido {quantidade_repeticoes} vezes é: ")
print(texto_repetido)