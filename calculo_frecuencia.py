colores = ["azul", "rojo", "verde", "azul", "rojo", "azul", "negro"]
conteo_colores = {}

for nota in colores:
    conteo_colores[nota] = conteo_colores.get(nota, 0) + 1
print(conteo_colores)