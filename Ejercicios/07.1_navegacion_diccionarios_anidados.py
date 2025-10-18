inventario_global = [
    {"tienda": "Norte", "productos": {"Monitor": 250.00, "Teclado": 45.50}},
    {"tienda": "Sur", "productos": {"Ratón": 18.00, "Gráfica": 300.00, "Webcam": 35.00}},
    {"tienda": "Centro", "productos": {"Monitor": 250.00, "Cargador": 20.00}}
]

# El resultado final DEBE ser un número único: 918.5

valor_total = 0

for tienda in inventario_global:
    for producto, precio in tienda["productos"].items():
        valor_total += precio
print("💰 Suma total del inventario global:", valor_total)
    