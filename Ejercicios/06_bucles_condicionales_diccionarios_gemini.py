inventario = {
    "monitor": 250.00,
    "teclado": 45.50,
    "ratón": 18.00,
    "gráfica": 300.00
}

for clave, valor in inventario.items():
    if valor > 200.00:
       print(f"¡GRAN DESCUENTO! El producto {clave} cuesta {valor} USD.")
    else:
        print(f"El producto {clave} tiene un precio normal")
        
temperaturas = [25, 30, -5, 35, 41, 28]

for temperatura in temperaturas:
    if temperatura < 0:
        continue
    if temperatura >= 40:
        break
    print(temperatura)

alumnos = [
    {"nombre": "Ana", "notas": [8, 9, 7]},
    {"nombre": "Luis", "notas": [6, 7, 8]},
    {"nombre": "Marta", "notas": [9, 10, 9]}
]

for alumno in alumnos:
    print(alumno["nombre"] + ":")

    lista_de_notas = alumno["notas"]
    for nota in lista_de_notas:
        print(" -Nota:", nota)