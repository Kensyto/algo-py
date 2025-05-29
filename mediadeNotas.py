# 5 - Calculando Média de Notas 📚

# Função auxiliar para solicitar e validar uma nota

def solicitar_nota(numero_da_nota):
    while True:
        try:
            # Solicita a nota e converte para float para permitir notas com casas decimais
            nota = float(input(f"Digite a nota {numero_da_nota}: "))
            # Opcional: Você pode adicionar uma validação para o intervalo da nota (ex: 0 a 10)
            if 0 <= nota <= 10: # Supondo que as notas são entre 0 e 10
                return nota
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota.")

# Solicita as três notas ao usuário usando a função auxiliar

nota1 = solicitar_nota(1)
nota2 = solicitar_nota(2)
nota3 = solicitar_nota(3)

# Calcula a média das notas
# O Copilot/ChatGPT é excelente para sugerir a fórmula básica da média: (soma) / quantidade
media = (nota1 + nota2 + nota3) / 3

# Exibe as notas digitadas e o resultado da média

print(f"\nAs notas digitadas foram: {nota1}, {nota2} e {nota3}")
print(f"A média das notas é: {media:.2f}") # Formata a média para duas casas decimais