import random
# Asignamos un numero para que la operación tenga un comienzo
one_number = 0
# El numero secreto sera asignado con el modulo que importamos al comienzo "random"
# y "randint" es la herramienta que utilizamos, una forma corta de usar (random_integer)
secret_number = random.randint(1, 100)
# Utilizamos "while" para crear el bucle y "!=" para expresar "no es igual"
while one_number != secret_number: 
# Agregamos input para que el usuario agregue el dato e int para que se convierta en el
# número entero que usaremos
    one_number = int(input("Enter a number: "))
# Condición if para que si el numero ingresado es igual al secreto, se acaba el juego.
    if one_number == secret_number:
        print("End Game, congratulations!")
# Condición elif si el número ingresado es menor sigue el juego y tira un mensaje con 
# el resultado.
    elif secret_number > one_number:
        print("The secret numbers is bigggest try again!")
# Condición elif si el número ingresado es mayor sigue el juego y tira un mensaje con 
# el resultado.
    elif secret_number < one_number:
        print("The secret number is smallest try again!")
        
# Y asi estan los datos, peticiones y las condiciones para que se ejecute el juego
# de las adivinanzas.