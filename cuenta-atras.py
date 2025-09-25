# Definimos la variable 'i' con un valor inicial de 10.
# 'i' será el contador para nuestra cuenta regresiva.
i = 10

# Usamos un bucle 'while' que se ejecuta mientras 'i' sea mayor o igual que 0.
# Esta es la condición que mantiene el bucle en marcha.
while i >= 0:
    # Imprimimos el valor actual de 'i' en cada iteración.
    print(i)

    # Restamos 1 a 'i' en cada paso para que la cuenta regrese.
    # Si no hiciéramos esto, el bucle sería infinito.
    i = i - 1

# Una vez que la condición del bucle deja de ser verdadera,
# el programa continúa y muestra este mensaje final.
print("Cuenta atrás finalizada")



# Definimos la variable 'i' con el valor inicial de 100.
# Esto es el punto de partida de la cuenta atrás.
i = 100

# Usamos un bucle 'while' que se ejecutará
# mientras el valor de 'i' sea mayor o igual que 0.
while i >= 0:
    # Imprimimos el valor actual de 'i'. El argumento 'end=" "'
    # evita el salto de línea y agrega un espacio en su lugar.
    print(i, end=" ")
    
    # Reducimos el valor de 'i' en 1 en cada iteración del bucle.
    # Esto es lo que hace que la cuenta atrás avance.
    i = i - 2

# Una vez que el bucle termina (cuando 'i' es -1),
# imprimimos el mensaje final en una nueva línea (\n).
print("\nCuenta atrás finalizada.")

