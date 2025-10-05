import math

first_number = int(input("First number: "))
second_number = int(input("Seconde number: "))

print("Selecciona una operación: ")
print("1. (+) ")
print("2. (-) ")
print("3. (*) ")
print("4. (/)")
print("5. (%)")
print("6. **")

operacion = input("Ingresa el número de la operación que deseas realizar: ")

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
else: 
    print("Operación no válida.")