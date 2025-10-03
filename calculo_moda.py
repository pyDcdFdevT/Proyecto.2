notas = [10, 8, 9, 7, 10, 8, 10, 9]
frecuencias = {}
for nota in notas:
    frecuencias[nota] = frecuencias.get(nota, 0) + 1
max_frecuencia = max(frecuencias.values())
moda = [nota for nota, freq in frecuencias.items() if freq == max_frecuencia]
print(moda)