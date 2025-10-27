# 1. El Dato Sucio (Cadena de Texto)
datos_sucios = "15.45 15.60 15.12 16.05 16.15 15.90 16.01 16.22 16.50 16.70"

# 2. Romper la Cadena en una Lista de STRINGS usando .split()
# El resultado es una lista, pero con los elementos como texto ("15.45", "15.60", etc.)
lista_de_strings = datos_sucios.split() 
# print(lista_de_strings) 
# Resultado: ['15.45', '15.60', '15.12', ...]

# 3. CONVERSIÓN: De Strings a Números (Flotantes)
# No podemos sumar texto, debemos convertir cada elemento a 'float' (decimal).
# Usamos una CLAVE DE PYTHON: la Comprensión de Listas (List Comprehension).
lista_de_numeros = [float(precio) for precio in lista_de_strings]
# print(lista_de_numeros)
# Resultado: [15.45, 15.6, 15.12, ...]

# --- Ahora podemos usar tu función flexible ---

# 4. Usar tu Función (pero necesitamos pasar la lista como *args)
# Para pasar una lista ya existente a una función que espera *args,
# ¡usamos el operador * otra vez! (Esto se llama 'Unpacking')

def sum_all_numbers(*numbers):
    final_sum = 0
    for number in numbers:
        final_sum += number
    print(f"La suma total es: {final_sum}")

print("\n--- Resultado Final ---")
# El *desempaqueta* la lista de números, enviando cada elemento por separado.
sum_all_numbers(*lista_de_numeros)