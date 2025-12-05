import pandas as pd
import numpy as np

# Datos de prueba (5 días de precios de cierre)
data = {'Close': [50.0, 50.8, 49.5, 51.2, 50.5]}
df_precios = pd.DataFrame(data)

# -----------------------------------------------------
# TU CÓDIGO AQUÍ (5 pasos en orden)
# -----------------------------------------------------

# 1. Calcule el Retorno Simple (SimpleReturn)
df_precios['Return'] = df_precios['Close'].pct_change()      

# 2. Elimine el NaN (df_limpio)
df_limpio = df_precios.dropna()

# 3. Filtre solo los días de PÉRDIDA (retorno < 0) (df_perdidas)
df_perdidas = df_limpio[df_limpio['Return'] < 0]

# 4. Calcule la media de df_perdidas (media_perdidas)
media_perdidas = df_precios['Return'].mean() 

# 5. Anualice la media (media_anualizada)
media_anualizada = media_perdidas * 252

# -----------------------------------------------------

# Imprimir el resultado final
print("--- Resultado Examen Final ---")
print(f"Retorno Medio de Pérdida (Diario): {media_perdidas:.4f}")
print(f"Retorno Medio de Pérdida (Anualizado): {media_anualizada:.2f}")