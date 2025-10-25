# Misión N° 6: El Valor Total de la Cartera

# Tu nuevo reto es calcular el valor monetario totalde una cartera,
# donde la información de la acción (símbolo) y su valor
# (valor_unitario y cantidad) están anidados en diccionarios.

cartera_inversor = {
    "acciones": [
        {"simbolo": "BBVA", "valor_unitario": 9.50, "cantidad": 500},
        {"simbolo": "TSLA", "valor_unitario": 250.00, "cantidad": 10},
        {"simbolo": "IBEX", "valor_unitario": 8000.00, "cantidad": 0.5} 
    ],
    "inversor": "pyDcdFdevT",
    "fecha": "2025-10-25"
}

# Variable que debe acumular el resultado:
valor_total_cartera = 0

for clave in cartera_inversor["acciones"]:
    valor = clave["valor_unitario"]
    cantidad = clave["cantidad"]
    simbolo = clave["simbolo"]
    valor_total_cartera += (valor * cantidad)
    print(f"El valor de {simbolo} = {valor * cantidad}")
print(f"\nEl valor total de la cartera es: {valor_total_cartera}")


    