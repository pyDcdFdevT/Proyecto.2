import math
#Proyecto de "Calculadora Científica" Estado. En Proceso

# "En este primer procedimiento defino primer número para luego utilizar int()
# y convertir lo que haya dentero en un número entero, lo cual va a ser la 
# base para mis operaciones siguentes, como se puede visualizar, utilizo input
# para que cuando ejecute el programa me pida los datos que necesito, con esto 
# hecho solo meto los demas datos para tener +,-,*,/"



primer_numero = int(input ("Primer número: "))
segundo_numero =int(input ("Segundo número: "))

suma = primer_numero + segundo_numero
#print(suma)

resta = primer_numero - segundo_numero
#print(resta)

multiplicacion = primer_numero * segundo_numero
#print(multiplicacion)

division = primer_numero / segundo_numero
#print(division)

#"Para poder sacar el porcentaje tuve que hacer una operación matemática basica
# el segundo número multiplicado por el primero para luego dividirlo entre 100
# eso me daría el resultado buscado"

porcentaje = (segundo_numero * primer_numero) / 100
#print(porcentaje)

# Potencia o raíz de x² se hace poniendo ** 

potencia = primer_numero ** segundo_numero
#print(potencia)

# Calcular Seno y Coseno
#print("\n--- Calculadora de Seno y Coseno ---")

#angulo_grados = int(input("Ingresa el número para el ángulo: "))

# "Convertimos los grados a radianes con el código de abajo ya que es lo que la 
# función math. sin() necesita" 

#angulo_radianes = math.radians(angulo_grados)

#seno = math.sin(angulo_radianes)
#coseno = math.cos(angulo_radianes)

# La función print() muestra un mensaje en la Terminal.
# La letra 'f' antes de las comillas crea un f-string.
# Un f-string te permite poner variables dentro del texto.
# Las llaves {} son los marcadores donde se reemplaza el texto con el valor de la variable.
# Por ejemplo: print(f"El resultado es: {variable}")

#print(f"El Seno de {angulo_grados} grados es: {seno}")
#print(f"El Coseno de {angulo_grados} grados es: {coseno}")

# "Damos control al usuario para que elija la operación a realizar
# Creamos el menú de opciones"

print("Selecciona una operación: ")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación *")
print("4. División (/)")
print("5. Porcentaje (%)")
print("6. Potencia (**)")
print("7. Seno (sin)")
print("8. Coseno (cos)")

# "Luego agregamos Seno y Coseno"

operacion = input ("Ingresa el número de la operación que deseas realizar: ")

if operacion == "1":
    print(suma)

elif operacion == "2":
    print(resta)

elif operacion == "3":
    print(multiplicacion)

elif operacion == "4":
    print(division)
    
elif operacion == "5":
    print(porcentaje)
    
elif operacion == "6":
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
    
# "RESUMEN DE TODO LO HECHO HASTA AHORA
#Desglose del Código

#El código se divide en tres partes principales: la configuración inicial, la interacción con el usuario y la lógica de las operaciones.

# 1. Configuración y Entrada de Datos

#import math: Esta línea es una declaración de importación. No es un comando que ejecutes en la Terminal, sino una instrucción para Python. Le dice al programa que quieres usar el "módulo" de matemáticas, que es una colección de funciones pre-hechas para operaciones avanzadas como seno y coseno.

#primer_numero = int(input(...)): Aquí usas la función input() para pedir un número al usuario. Lo que el usuario escribe se guarda como un string (texto), por lo que usas int() para convertirlo a un número entero que Python pueda usar en cálculos.

#segundo_numero = int(input(...)): Haces lo mismo para el segundo número.

#2. Interfaz y Menú

#print("Selecciona una operación: "): Estas líneas son tu interfaz de usuario. Le muestran al usuario las opciones disponibles de una manera clara y legible.

#operacion = input(...): Esta línea espera a que el usuario elija una opción. La elección del usuario se guarda en la variable operacion como un string (por ejemplo, "1", "2", etc.).

#3. Lógica de las Operaciones

#Aquí es donde usas la lógica condicional para controlar el flujo de tu programa.

#if operacion == "1":: El programa evalúa si el valor en la variable operacion es igual al string "1". Si es verdadero, ejecuta el código que está indentado debajo. Si no, salta al siguiente bloque elif.
#print(primer_numero + segundo_numero): Esta línea combina la operación de suma y la función de impresión en una sola. Python realiza el cálculo primer_numero + segundo_numero y el resultado se imprime directamente en la Terminal.

#elif operacion == "2":: Este bloque es similar al if pero solo se evalúa si el if anterior fue falso. Este patrón se repite para todas las operaciones (resta, multiplicación, etc.).

#elif operacion == "5": (Módulo): Aquí utilizas el operador %. Su función es devolver el residuo de una división. Por ejemplo, 20 % 4 es 0 porque no hay residuo.

#elif operacion == "6": (Potencia): Usas el operador ** para elevar un número a la potencia de otro. En tu ejemplo, 20 ** 4 da como resultado 160000.

#elif operacion == "7": (Seno):angulo_grados = int(input(...)): Dentro de este bloque, pides un nuevo número porque el seno solo necesita un ángulo.
#angulo_radianes = math.radians(angulo_grados): Esta es una función del módulo math que convierte el ángulo de grados a radianes, que es la unidad que las funciones sin y cos necesitan para funcionar.
#print(math.sin(angulo_radianes)): Imprimes el resultado de la función math.sin().

#elif operacion == "8": (Coseno): Funciona exactamente igual que el seno, usando la función math.cos()."