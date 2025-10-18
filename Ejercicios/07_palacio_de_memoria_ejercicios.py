###-------------- EL NIÑO FOR --------------###
#EJERCICIO 1
animales = ["gato", "perro", "conejo", "tortuga"]

# Tu misión: haz que el niño For diga "El niño For juega con [animal]"

for animal in animales:
    print(f"El niño For juega con {animal}")

#EJERCICIO 2
numeros = [1, 2, 3, 4, 5]

# Tu misión: que For diga el doble de cada número

dobles = [x * 2 for x in numeros]
print(f"El niño For multiplicó por dos cada número de la lista: {numeros} dando como resultado: {dobles}") 

###-------------- EL GUARDIAN WHILE --------------###

#EJERCICIO 3
# Tu misión: mientras el reloj sea menor que 5, que diga el número
i = 0
while i < 5:
    print("El guardian while cuenta:", i)
    i += 1

#EJERCICIO 4
# El Guardián While cuida la puerta del castillo y deja pasar 
# a los visitantes hasta que lleguen 3.
# Simúlalo imprimiendo un mensaje de “Visitante X ha entrado”.

v = 1
while v <= 3:
    print(f"Visitante {v} ha entrado")
    v += 1
    
###-------------- EL MAESTRO RANGE --------------###

#EJERCICIO 5
# El Maestro Range quiere contar los números del 1 al 5.
# Haz que lo haga con un bucle for y range().

for numero in range(1, 6):
    print(f"El maestro Range cuenta: {numero}")

#EJERCICIO 6
# El Maestro Range quiere enseñar los números pares del 2 al 10.
# Usa los tres pergaminos mágicos: inicio, fin y paso.

for numero in range(2, 11, 2):
    print(f"El maestro Range cuenta: {numero}")
    
###-------------- LOS GEMELOS BREAK Y CONTINUE --------------###

#EJERCICIO 7
# El Maestro Range cuenta del 1 al 10,
# pero Break lo detiene cuando llega al 6.

for cuenta in range(1,11):
    if cuenta == 6:
        print("¡Detente ahí! ⚡ (Break ha intervenido)")
        break
    print(cuenta)

#EJERCICIO 8
# El Maestro Range cuenta del 1 al 5,
# pero Continue le dice que se salte el número 3

for numero in range(1, 6):
    if numero == 3:
        print("Saltamos este número ⚡ (Continue en acción)")
        continue
    print(numero)
    
###-------------- GUARDIANES DE LAS DECICIONES IF, ELIF, ELSE --------------###

#EJERCICIO 9
# El Guardián If cuida la entrada del palacio.
# Solo deja pasar a mayores de edad (18 o más).

edad = int(input("Cuál es tu edad? "))
if edad >= 18:
    print("¡Puedes entrar!🏰")
else:
    print("¡No puedes entrar!🚫")
    
#EJERCICIO 10
# El consejero Elif observa el clima:
# Si hace más de 30 grados → “Hace calor 🌞”
# Si hace más de 20 → “Hace buen tiempo 🌤️”
# Si hace más de 10 → “Hace fresco 🍃”
# Si no → “Hace frío ❄️”

temperatura = int(input("¿Qué temperatura hace? "))
if temperatura > 30:
    print("Hace calor🌞")
elif temperatura > 20:
    print("Hace buen tiempo🌤️")
elif temperatura > 10:
    print("Hace fresco🍃")
else:
    print("Hace frío🥶")
    
#EJERCICIO 11
# EL JUEZ ELSE EVALÚA NOTAS:
# 9 o más → “Excelente 🏆”
# 6 a 8 → “Aprobado ✅”
# Menos de 6 → “Suspendido ❌”

nota = int(input("¿Que nota haz sacado? "))
if nota >= 9:
    print("¡Excelente! 🏆")
elif nota >= 6:
    print("Aprobado✅")
else:
    print("Suspendido ❌")

###-------------- LOS ARQUITECTOS: LISTAS, DICCIONARIOS, TUPLAS Y CONJUNTOS --------------###

#EJERCICIO 12 "LAS LISTAS"
tesoros = ["moneda de oro", "copa de plata", "zafiro", "diamante"]
for tesoro in tesoros:
    print(f"El niño for ha encontrado: {tesoro}")    

#EJERCICIO 13 
# Agrega un nuevo tesoro con .append(),
# y luego ordénalos con .sort().

tesoros.append("corona de oro")
tesoros.sort()
print("Los tesoros ordenados son:", tesoros)

#EJERCICIO 14 "LOS DICCIONARIOS"

# Crea un diccionario llamado personaje con:
# nombre
# edad
# oficio
# Imprime su nombre usando su clave.

personaje ={"nombre":"Máximo", "edad":77, "oficio":"comandante"}
print("El nombre del personaje es:", personaje["nombre"])

#EJERCICIO 15 
# Usa un bucle for con .items() para que el sabio lea cada dato:

for clave, valor in personaje.items():
    print(f"La clave es: {clave} y su valor es: {valor}")
    
#EJERCICIO 16 "LAS TUPLAS"
# Crea una tupla llamada cofre_sagrado con tres tesoros.
# Intenta cambiar uno y observa lo que pasa.

cofre_sagrado = ("corona", "moneda", "cáliz")
#cofre_sagrado.appened("zafiro")
print(cofre_sagrado)

#LAS TUPLAS NO PUEDEN SER CAMBIADAS O ALTERADAS❌
# Nota: las tuplas no pueden modificarse; si necesitas añadir, usa una lista.

#EJERCICIO 17 "LOS CONJUTNTOS"
# Crea un conjunto flores = {"rosa", "margarita", "rosa"}
# Imprime el resultado y observa cómo elimina los duplicados.

flores = {"rosa", "margarita", "rosa"}
print(flores) # Elimina duplicados automáticamente

#EJERCICIO 18 Usa .intersection() y .union() para ver:
# Las flores que comparten 🌸
# Las que se unen 🌷

jardin_1 = {"rosa", "lirio", "tulipán"}
jardin_2 = {"lirio", "margarita", "clavel"}

print("Unión:", jardin_1.union(jardin_2))
print("Intersección:", jardin_1.intersection(jardin_2))

###-------------- MAGOS DE LA FUNCIÓN --------------###

#EJERCICIO 19 "DEF EL MAGO QUE CREA HECHIZOS" 
# ACTIVAR Y LLAMAR A LA MAGIA"
# Crea una función saludar(nombre) que diga “Hola [nombre] del Palacio”.

def saludar(nombre): 
    print("Hola,", nombre, "bienvenid al Palacio 🏰")
saludar("CodigoSinBugs")

#EJERCICIO 20 "EL MAGO QUE DEVUELVE LA MAGIA"

def sumar(a,b):
    return a + b
resultado = sumar(77, 33)
print("El resultado de la suma mágica es:", resultado)

#EJERCICIO 21 "RETO MÁGICO"
# Crea una función evaluar_nota(nota) que:
# Devuelva “Excelente” si ≥ 9
# Devuelva “Aprobado” si ≥ 6
# Devuelva “Reprobado” si < 6
# Y luego llama a la función con distintos valores.

def evaluar_nota(nota):
    if nota >= 9:
        return "¡Excelente!🤩"
    elif nota >= 6:
        return "¡Aprobado!✅"
    else:
        return "Reprobado❌"
resultado = evaluar_nota(5)
print("El resultado del examen es: ", resultado)

#EJERCICIO 22 "MAGO AVANZADO"
# Crea una función contar_tesoros(lista_tesoros)
# que recorra una lista con for y diga cuántos hay.

def contar_tesoros(lista_tesoros):
    cantidad = 0
    for tesoro in lista_tesoros:
        cantidad += 1
        print("He encontrado:", tesoro)
    print("Total de tesoros encontrados:", cantidad)

lista_tesoros = ["oro", "plata", "diamante", "esmeralda", "oro", "rubí", "zafiro"]  
  
contar_tesoros(lista_tesoros)

# 🌟 MODO DESAFÍO — “EL PALACIO VIVO”
# Misión final:
# Crea un programa que combine todo lo aprendido:
# Usa una lista de habitantes del palacio
# Usa un bucle for para presentarlos
# Si alguno es “Mago”, crea una función hechizo() que lo haga hablar
# Usa if, elif, else para que respondan diferente según su rol
# Termina cuando el Guardián While diga que es hora de dormir ⏰

habitantes_del_palacio = {
    "for":"El niño que juega con todo", "while":"El Guardian que repite hasta que algo cambia",
    "range":"El maestro que controla los números", "break":"El gemelo que interrumpe el ciclo",
    "continue":"El gemelo que salta una vuelta del ciclo", "if":"El guardian que solo responde a la verdad",
    "elif":"El consejero que da opciones", "else":"El juez final", "listas":"Los cofres ordenados",
    "diccionarios":"Los archivos del sabio", "tuplas":"Los cofres sellados", "conjuntos":"Los jardines sin duplicados",
    "def":"El mago que crea hechizos", "return":"El mago que devuelve la magia", "nombre_del_hechizo": "El que activa la magia"
}

for clave, valor in habitantes_del_palacio.items():
    print(f"Mi nombre es {clave} y soy {valor}")

def el_mago_dice(mago):
    if mago == "def":
        return "Soy el mago que crea hechizos."
    elif mago == "return":
        return "Soy el mago que devuelve los hechizos."
    else:
        return "Soy el que activa la magia"

print(el_mago_dice("def"))
print(el_mago_dice("return"))
print(el_mago_dice("otra cosa"))

i = 5
while i > 0:
    print("El guardian while dice que hay que dormir en:", i)
    i -= 1
print("💤 Todos los habitantes del Palacio descansan... Fin del viaje.")