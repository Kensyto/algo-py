# 3 - Operações Matemáticas Simples 📐

# Solicita o primeiro número ao usuário

while True: # Loop para garantir que a entrada é um número válido
    try:
        num1 = float(input("Digite o primeiro número: "))
        break # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Solicita o segundo número ao usuário

while True: # Loop para garantir que a entrada é um número válido
    try:
        num2 = float(input("Digite o segundo número: "))
        break # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Solicita a operação desejada ao usuário

operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação com base na escolha do usuário

if operacao == '+':
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"A subtração de {num1} por {num2} é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"A multiplicação de {num1} por {num2} é: {resultado}")
elif operacao == '/':
    # Verifica se o segundo número não é zero antes de dividir
    if num2 != 0:
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")