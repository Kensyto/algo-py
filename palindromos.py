# 6 - Verificando Palíndromos 🔄

# Solicita uma palavra ou frase ao usuário
palavra_ou_frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

# --- Etapa de Normalização (para uma verificação mais robusta) ---
# Remove espaços e converte tudo para minúsculas.

palavra_limpa = palavra_ou_frase.replace(" ", "").lower()
# Ex: "Arara" -> "arara", "A mala na cama" -> "amalanacama"

# Inverte a palavra ou frase limpa

palavra_invertida = palavra_limpa[::-1]
# Ex: "arara" -> "arara", "amalanacama" -> "amalanacama"

# Verifica se a palavra/frase original (limpa) é igual à sua versão invertida

if palavra_limpa == palavra_invertida:
    print(f"'{palavra_ou_frase}' é um PALÍNDROMO! 🎉")
else:
    print(f"'{palavra_ou_frase}' NÃO é um palíndromo. 😞")