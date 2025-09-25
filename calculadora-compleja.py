import math
first_number = int(input ("Primer número: "))
second_number =int(input ("Segundo número: "))

print("Selecciona una operación: ")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación *")
print("4. División (/)")
print("5. Porcentaje (%)")
print("6. Potencia (**)")
print("7. Seno (sin)")
print("8. Coseno (cos)")

operacion = input ("Ingresa el número de la operación que deseas realizar: ")

if operacion == "1":
    suma = first_number + second_number
    print(suma)
elif operacion == "2":
    resta = first_number - second_number
    print(resta)
elif operacion == "3":
    multiplicacion = first_number * second_number
    print(multiplicacion)
elif operacion == "4":
    if second_number == 0:
        print("Error. NO se puede dividir por cero.")
    division = first_number / second_number
    print(division)
elif operacion == "5":
    modulo = first_number % second_number
    print(modulo)
elif operacion == "6":
    potencia = first_number ** second_number
    print(potencia)
    
elif operacion == "7":
    angulo_grados = int(input("Ingresa el número para el ángulo: "))
    angulo_radianes = math.radians(angulo_grados)
    seno = math.sin(angulo_radianes)
    print(seno)
    
elif operacion == "8":
    angulo_grados = int(input("Ingresa el número para el ángulo: "))
    angulo_radianes = math.radians(angulo_grados)
    coseno = math.cos(angulo_radianes)
    print(coseno)

else: 
    print("Operación no válida.")