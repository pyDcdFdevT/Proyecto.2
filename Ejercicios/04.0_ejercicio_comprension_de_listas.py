#El 'Por Qué' de la Comprensión de Listas
#La gran ventaja de la Comprensión de Listas es que te permite 
# aplicar esa lógica de acceso uno-por-uno a todos los elementos 
# del diccionario, ¡todo en una sola línea de código!

#La Comprensión de Listas es el atajo de Python para hacer el
# bucle + extracción + adición a la lista, lo que la hace más rápida
# de escribir y, a menudo, más rápida de ejecutar que un bucle for tradicional.

#Ejercicio 1/3: Versión Pythonic
#Ahora, usa esa lógica de doble indexación (datos[0] o datos[1])
#y aplícala a la Comprensión de Listas.

clientes = {
    "Ana": ["España", 1250],
    "Luis": ["México", 800],
    "Marta": ["España", 2100],
    "Pedro": ["Colombia", 950]
}

#.items() Devuelve una vista de pares clave-valor del diccionario
# en forma de tuplas. Cada elemento devuelto es una tupla con dos valores:
#(clave, valor)

# 1. Lista de Países (Usa datos[0] para acceder a "España", "México", etc.)
lista_paises = [datos[0] for nombre, datos in clientes.items()] 



# 2. Lista de Saldos (Usa datos[1] para acceder a 1250, 800, etc.)
lista_saldos = [datos[1] for nombre, datos in clientes.items()]

print("Países:", lista_paises)
print("Saldos:", lista_saldos)