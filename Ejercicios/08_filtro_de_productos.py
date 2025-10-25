#Misión N° 4: El Filtro de Productos 
#Objetivo: Recorrer la lista de diccionarios pedidos. 
#Detener la búsqueda inmediatamente usando break si la cantidad es menor a 2.


pedidos = [
    {"item": "Camisa", "cantidad": 5, "urgencia": False},
    {"item": "Pantalón", "cantidad": 10, "urgencia": False},
    {"item": "Zapatos", "cantidad": 1, "urgencia": True},  # ¡El break debe actuar aquí!
    {"item": "Corbata", "cantidad": 8, "urgencia": False}
]

for pedido in pedidos:
    item = pedido["item"]         # 1. Acceso a la etiqueta "item"
    cantidad = pedido["cantidad"] # 2. Acceso directo a la etiqueta "cantidad"

    if cantidad < 2:
        # El Gemelo Break interviene
        print(f"⚠️ ALERTA DE STOCK BAJO! Pedido detenido en {item} (Stock: {cantidad})")
        break
    else:
        # Se sigue con el bucle
        print(f"✅ {item} tiene stock suficiente.")

print("Búsqueda finalizada.")