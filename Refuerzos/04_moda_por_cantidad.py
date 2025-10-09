pedidos = {
    "P001": {"producto": "Teclado", "cantidad": 5, "precio_unitario": 25.0, "entregado": True},
    "P002": {"producto": "Monitor", "cantidad": 2, "precio_unitario": 150.0, "entregado": False},
    "P003": {"producto": "Mouse", "cantidad": 10, "precio_unitario": 15.0, "entregado": True},
    "P004": {"producto": "Teclado", "cantidad": 3, "precio_unitario": 25.0, "entregado": False},
    "P005": {"producto": "Mouse", "cantidad": 7, "precio_unitario": 15.0, "entregado": True}
}

conteo_demanda = {}

# 1. Bucle que itera sobre la CLAVE y el DICCIONARIO INTERNO
for id_pedido, datos_pedido in pedidos.items():
    
    # 2. Extraer el nombre del producto (la CLAVE de nuestro nuevo diccionario)
    producto = datos_pedido["producto"]
    
    # 3. Extraer la cantidad a SUMAR
    cantidad = datos_pedido["cantidad"]
    
    # 4. Usar .get() para sumar las cantidades acumuladas
    #    Si 'producto' existe en el diccionario, suma 'cantidad' a su valor actual.
    #    Si NO existe (es la primera vez), empieza desde 0 + cantidad.
    conteo_demanda[producto] = conteo_demanda.get(producto, 0) + cantidad


print("--- RESULTADO DEL CONTEO ---")
print(conteo_demanda)

producto_mas_demandado = max(conteo_demanda, key =conteo_demanda.get)
print(f"\n✅ Producto más demandado: {producto_mas_demandado}")