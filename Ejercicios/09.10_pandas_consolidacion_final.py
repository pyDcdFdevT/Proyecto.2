import pandas as pd
import numpy as np

# Datos para la prueba
precios_test = [20.0, 20.5, 19.9, 21.0, 21.15, 20.8]

# -----------------------------------------------------
# TU CÓDIGO AQUÍ
# -----------------------------------------------------

# 1. Define la función 'preparar_datos_quant(precios)'
def preparar_datos_quant(precios):
    df = pd.DataFrame({'Price': precios})
    df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
    df = df.dropna()
    return df
    
    
# 2. Llama a la función y muestra el DataFrame resultante
df_final = preparar_datos_quant(precios_test)
print("--- DataFrame Final Limpio (Ejercicio 10/10) ---")
print(df_final)