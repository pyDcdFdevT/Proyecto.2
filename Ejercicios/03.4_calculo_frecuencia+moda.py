colores = ["azul", "rojo", "verde", "azul", "rojo", "azul", "negro"]
conteo_colores = {}
for nota in colores:
    conteo_colores[nota] = conteo_colores.get(nota, 0) + 1
max_frecuencia = max(conteo_colores.values())
print(max_frecuencia)
moda = [nota for nota, freq in conteo_colores.items() if freq == max_frecuencia]
print(moda)