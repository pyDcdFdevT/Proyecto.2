# --- CÓDIGO DE PANDAS QUE DEBE ESTAR AL FINAL ---
import pandas as pd # <--- ¡Asegúrate de que está!

cartera_inversor = {
    "acciones": [
        {"simbolo": "BBVA", "valor_unitario": 9.50, "cantidad": 500},
        {"simbolo": "TSLA", "valor_unitario": 250.00, "cantidad": 10},
        {"simbolo": "IBEX", "valor_unitario": 8000.00, "cantidad": 0.5} 
    ],
    "inversor": "pyDcdFdevT",
    "fecha": "2025-10-25"
}

lista_acciones = cartera_inversor["acciones"]

# CREA EL DATAFRAME
df_cartera = pd.DataFrame(lista_acciones)

# IMPRIME EL DATAFRAME
print("--- DATAFRAME DE CARTERA QUANT ---")
print(df_cartera.head())