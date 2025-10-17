### LOOPS ###

#---------------     While     ----------------#

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)
    
print("La ejecución continúa")

#---------------     For    ----------------#
# For Itera sobre cualquier objeto iterable (Lista, Tupla, Conjunto, Diccionario, etc.).
# En el caso de un Diccionario, por defecto, itera SOLAMENTE sobre las CLAVES.
# Para obtener los VALORES, se debe usar el método .values().
# Para obtener AMBOS (Clave y Valor) a la vez, se debe usar el método .items().

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: 
    print(element)
    
my_tuple = (28, 1.74, "Codigo", "SinBugs", "Codigo")

for element in my_tuple: 
    print(element)

my_set = {"Codigo", "Codigo", 28}

for element in my_set: 
    print(element)

my_dict = {"Nombre":"Codigo", "Apellido":"Sinbugs", "Edad":28, 1:"Python"}

for element in my_dict: #IMPRIME CLAVE 
    print(element)

for element in my_dict.values(): #IMPRIME VALOR
    print(element)

for clave, valor in my_dict.items(): #IMPRIME CLAVE Y VALOR
    print(f"{clave}: {valor}")
    print(f"Clave: {clave}, Valor: {valor}")

#my_dict_2 = {"Nombre":"Codigo", "Apellido":"Sinbugs", "Edad":28, 1:"Python"}

#for element in my_dict_2:
    #print(element)
   # if element == "Edad":
       # continue
    #print("Se ejecuta")
#else:
   # print("El bucle for para mi diccionario ha finalizado")
    