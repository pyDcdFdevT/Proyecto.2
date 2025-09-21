#------------------------->MINI-CALCULADORA<-------------------#
primer_numero = input("Escribe el primer número: ")
segundo_numero = input("Escribe el segundo número")

primer_numero_int = int(primer_numero)
segundo_numero_numero_int = int(segundo_numero)

# Suma de los dos números 
resultado_suma = primer_numero_int + segundo_numero_numero_int

# Resta de los dos números 
resultado_resta = primer_numero_int - segundo_numero_numero_int

# Multiplicación de los dos números
resultado_multiplicacion = primer_numero_int * segundo_numero_numero_int

# División de los dos números
resultado_division = primer_numero_int / segundo_numero_numero_int


print(f"La suma es: {resultado_suma}")
print(f"La resta es: {resultado_resta}")
print(f"La multiplicación es: {resultado_multiplicacion}")
print(f"La división es: {resultado_division} ")