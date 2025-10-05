frase = "Data Science es el futuro"
frase_invertida = frase[::-1]
print(frase_invertida)

# 1. Encontrar el índice del espacio ANTES de "futuro"
# Usaremos .rfind() que busca desde el final hacia el inicio.
# Busca el último espacio.
indice_ultimo_espacio = frase.rfind(" ")

# 2. Extracción de "futuro" usando el índice encontrado y el final de la cadena
# [indice_ultimo_espacio + 1 :]
# Esto significa: empieza un carácter después del último espacio, y ve hasta el final.
palabra_futuro = frase[indice_ultimo_espacio + 1 :]

# 3. Imprimimos el resultado (que ahora es flexible)
print(f"La palabra 'futuro' extraída de forma flexible es: {palabra_futuro}")
# Output: La palabra 'futuro' extraída de forma flexible es: futuro
