
#creando una lista (se puede modificar)
lista = ["Diego Toledo","diegofetv",True,1.74]

#creando una tupla (no se puede modificar)
tupla = ("Diego Toledo","diegofetv",True,1.74)

#esto es válido
#lista[3]= "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (caracteristicas: no se puede accede a los elementos por indice, no almacena datos duplicados, pueden ser o son datos desordenado)
conjunto = {"Diego Toledo","diegofetv",True,1.74}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) (la estructura es key : value y separamos con comas, si solo hay un elemento no se ponen comas, si hay muchos o varios elementos se ponen tantas comas como elementos -1)
diccionario = {
    'nombre' : "Diego Toledo",
    'instagram' : "diegofetv",
    'esta_emocionado' : True,
    'altura' : 1.74,
    'dato_duplicado' : "diegofetv" 
    }

print(diccionario["altura"] + 2)
print(lista[3])

