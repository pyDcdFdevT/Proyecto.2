pedidos = {
    "P001": {"producto": "Teclado", "cantidad": 5, "precio_unitario": 25.0, "entregado": True},
    "P002": {"producto": "Monitor", "cantidad": 2, "precio_unitario": 150.0, "entregado": False},
    "P003": {"producto": "Mouse", "cantidad": 10, "precio_unitario": 15.0, "entregado": True},
    "P004": {"producto": "Teclado", "cantidad": 3, "precio_unitario": 25.0, "entregado": False},
    "P005": {"producto": "Mouse", "cantidad": 7, "precio_unitario": 15.0, "entregado": True}
}

valor_pendiente = 0

# --- CÓDIGO A COMPLETAR ---
for clave_pedido, datos_pedido in pedidos.items():
    if datos_pedido["entregado"] == False:
        subtotal = datos_pedido["cantidad"] * datos_pedido["precio_unitario"]
        valor_pendiente += subtotal

print(f"Valor pendiente de entrega: {valor_pendiente} USD")