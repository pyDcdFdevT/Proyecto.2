# Archivo: Ejercicios/09.7_pandas_nan_drop_y_anualizacion.py

import pandas as pd
import numpy as np

# 1. Datos de ejemplo (precios de cierre)
data = {'Close': [100.0, 101.5, 99.8, 103.0, 102.1]}
df = pd.DataFrame(data)

# 2. CALCULAR LOG-RETURN
df['Return_log'] = np.log(df['Close'] / df['Close'].shift(1))

# -----------------------------------------------------
# TU CÓDIGO AQUÍ (Sección 7 y 5 de la lección)
# -----------------------------------------------------

# A. Elimina la fila NaN y copia el DF limpio a 'df_clean'.
#    Pista: usa df.dropna(subset=['Return_log']).copy()

df_clean = ...

# B. Calcula la media diaria (mean_log) y la desviación estándar diaria (std_log)
#    (Ambos sobre df_clean['Return_log'])

mean_log = ...
std_log = ...

# C. Anualiza las métricas
N_DIAS = 252
mean_annual = ... # Multiplicación simple
vol_annual = ...  # Multiplicación por la raíz de N_DIAS

# D. Imprime los resultados
print(f"Media Diaria (Log): {mean_log:.6f}")
print(f"Volatilidad Diaria (Log): {std_log:.6f}")
print("---")
print(f"Retorno Anualizado (Log): {mean_annual:.4f}")
print(f"Volatilidad Anualizada: {vol_annual:.4f}")