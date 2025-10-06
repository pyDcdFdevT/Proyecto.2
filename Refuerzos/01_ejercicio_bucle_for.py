# 1. Crea un bucle 'for' que itere sobre los ÍNDICES (0, 1, 2...)
# de la lista 'precios'.
#    Pista: ¿Qué combinación de funciones te da los índices de la lista?
# 2. Dentro del bucle, usa el índice para acceder al elemento actual.
# 3. MODIFICA el valor original en ese índice, aumentándolo en un 10% 
# (multiplica por 1.10).
#    Fórmula: precios[i] = precios[i] * 1.10

precios = [50, 120, 35, 80, 150]
for i in range(len(precios)):
    precio_original = precios[i]
    precio_nuevo = precio_original * 1.10
    precio_nuevo = round(precio_nuevo, 2)
    precios[i] = precio_nuevo
print("\n --- LISTA MODIFICADA (Aumento del 10%) ---")
print(precios)

# Lista de precios (resultante del Ejercicio 1/2, ya modificada)
precios_finales = [55.0, 132.0, 38.5, 88.0, 165.0]
print("\n--- REPORTE DE INVENTARIO CON ENUMERATE ---")

# 1. Crea un bucle 'for' que use la función 'enumerate()' sobre 'precios_finales'.
#    El bucle debe extraer DOS variables: el índice (i) y el precio (p).
#    Pista: for i, p in enumerate(lista):

# 2. Dentro del bucle, usa un 'print()' con una f-string para mostrar:
#    "El artículo en la posición [i] vale [p] USD."

for i, p in enumerate(precios_finales):
    print(f"El artículo en la posición {i} vale {p} USD.")



