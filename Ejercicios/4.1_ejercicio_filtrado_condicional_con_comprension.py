# Ejercicio 2/3: Filtrado Condicional con Comprensión
#El objetivo de este ejercicio es combinar la Comprensión 
#de Listas con una condición (if) para crear una nueva 
#lista basada en un criterio. Esto es crucial para la limpieza 
#y preparación de datos.

#Contexto: Tienes un registro de productos con sus existencias.
#Quieres saber qué productos están con menos de 100 unidades
#en el inventario para poder reponerlos.

#Tu Tarea (CÓDIGO):
#Crea una lista llamada productos_bajos.
#Utiliza Comprensión de Listas para que esta lista contenga solo
# el CÓDIGO del producto ("A101", "B205", etc.)
#Aplica una condición if para incluir el código solo si el valor 
# de existencias es menor a 100.

#Pista: La estructura de Comprensión de Listas con condición es:
# [EXPRESIÓN for CLAVE, VALOR in dic.items() if CONDICIÓN].

#Diccionario de Entrada:
inventario = {
    "A101": ["Teclado Mecánico", 150],
    "B205": ["Monitor Curvo", 85],
    "C303": ["Mouse Gaming", 300],
    "D401": ["Webcam 4K", 98],
    "E505": ["Micrófono USB", 120]
}
productos_bajos = [codigo for codigo, valor in inventario.items() if valor[1] < 100]
print(productos_bajos)

