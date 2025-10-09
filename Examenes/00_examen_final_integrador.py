pedidos = {
    "P001": {"producto": "Teclado", "cantidad": 5, "precio_unitario": 25.0, "entregado": True},
    "P002": {"producto": "Monitor", "cantidad": 2, "precio_unitario": 150.0, "entregado": False},
    "P003": {"producto": "Mouse", "cantidad": 10, "precio_unitario": 15.0, "entregado": True},
    "P004": {"producto": "Teclado", "cantidad": 3, "precio_unitario": 25.0, "entregado": False},
    "P005": {"producto": "Mouse", "cantidad": 7, "precio_unitario": 15.0, "entregado": True}
}

def analizar_pedidos(diccionario_pedidos):
    
    # Variables de salida
    total_entregado = 0  
    productos_pendientes = [] 
    conteo_demanda = {} # Diccionario para calcular la Moda por Cantidad

    # 1️⃣ BUCLE PRINCIPAL
    for clave_pedido, datos_pedido in diccionario_pedidos.items():
        
        # Objetivo 1: Sumar el VALOR TOTAL de pedidos ENTREGADOS
        if datos_pedido["entregado"]:
            total_entregado += datos_pedido["cantidad"] * datos_pedido["precio_unitario"]
        
        # Objetivo 2: Crear la LISTA de productos PENDIENTES
        if not datos_pedido["entregado"]:
            productos_pendientes.append(datos_pedido["producto"])
        
        # Objetivo 3: SUMAR las cantidades en el diccionario conteo_demanda
        producto = datos_pedido["producto"]
        cantidad = datos_pedido["cantidad"]
        conteo_demanda[producto] = conteo_demanda.get(producto, 0) + cantidad
    
    # 2️⃣ Después del bucle: Calcular la MODA (producto más demandado)
    producto_mas_demandado = max(conteo_demanda, key=conteo_demanda.get)
    
    # 3️⃣ Devolver los resultados
    return total_entregado, productos_pendientes, producto_mas_demandado

# Llamada a la función
valor_total, lista_pendientes, producto_moda = analizar_pedidos(pedidos)

print(f"1. Valor Total Entregado: {valor_total} USD")
print(f"2. Productos Pendientes: {lista_pendientes}")
print(f"3. Producto Más Demandado: {producto_moda}")
