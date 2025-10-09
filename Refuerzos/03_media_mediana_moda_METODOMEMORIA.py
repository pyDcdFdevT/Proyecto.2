datos = [10, 10, 20, 30, 30, 30, 40, 50]
frecuencia = {}

L = len(datos)
indice_1 = (L // 2) - 1
indice_2 = (L // 2) 
valor_1 = datos[indice_1]
valor_2 = datos[indice_2]
mediana = (valor_1 + valor_2) / 2    #R = 30.0

for nota in datos:
    frecuencia[nota] = frecuencia.get(nota, 0) + 1
max_frecuencia = max(frecuencia.values())
moda = [nota for nota, freq in frecuencia.items() if freq == max_frecuencia]

suma_todo_datos = sum(datos)
mediana = suma_todo_datos / L
print(mediana)
