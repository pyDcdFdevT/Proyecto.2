#🎯 Misión del Día 20: Aplicación Quant (09:28 AM)
#Acabas de ver el concepto de return y el uso de parámetros.
#Ahora, vamos a aplicar esto a tu proyecto:

#La Misión es tomar el script de tu cartera y transformarlo
# en una función que acepte la cartera como parámetro y
# devuelva el valor total (usando return).

#🧠 El Desafío (Recuerda tu Lógica)

#Tu código anterior usaba una lista de diccionarios anidados. La función debe:
#Definición: Empezar con def calcular_valor_cartera(cartera):.
#Lógica: Usar el bucle for para iterar sobre cartera["acciones"].
#Resultado: Usar return para devolver el acumulador final.
#Tu tarea es completar la función a continuación y luego demostrar
# cómo la ejecutas para obtener el valor final:

cartera_inversor = {
    "acciones": [
        {"simbolo": "BBVA", "valor_unitario": 9.50, "cantidad": 500},
        {"simbolo": "TSLA", "valor_unitario": 250.00, "cantidad": 10},
        {"simbolo": "IBEX", "valor_unitario": 8000.00, "cantidad": 0.5} 
    ],
    "inversor": "pyDcdFdevT",
    "fecha": "2025-10-25"
}

# 1. DEFINE LA FUNCIÓN AQUI, ACEPTANDO 'cartera' COMO PARÁMETRO
def calcular_valor_cartera(cartera):

    # 2. INICIALIZA EL ACUMULADOR AQUI
    valor_total_cartera = 0
    

    # 3. USA TU BUCLE FOR PARA ITERAR SOBRE cartera["acciones"]
    for clave in cartera["acciones"]:

    # 4. CALCULA Y ACUMULA EL VALOR
        valor = clave["valor_unitario"]
        cantidad = clave["cantidad"]
        valor_total_cartera += valor * cantidad

    # 5. USA RETURN PARA DEVOLVER EL VALOR TOTAL
    return valor_total_cartera


# 6. LLAMA A LA FUNCIÓN Y GUARDA EL RESULTADO EN UNA VARIABLE
valor_final_quant = calcular_valor_cartera(cartera_inversor)

# 7. IMPRIME EL RESULTADO FINAL (fuera de la función)
print(f"La cartera de {cartera_inversor['inversor']} tiene un valor total de: {valor_final_quant}$")