# Archivo: Ejercicios/09.7_pandas_nan_drop_y_anualizacion.py

import pandas as pd
import numpy as np

# 1. Datos de ejemplo (precios de cierre)
data = {'Close': [100.0, 101.5, 99.8, 103.0, 102.1]}
df = pd.DataFrame(data)

# 2. CALCULAR LOG-RETURN
df['Return_log'] = np.log(df['Close'] / df['Close'].shift(1))

df_clean = df.dropna(subset=['Return_log']).copy()

# B. Calcula la media diaria (mean_log) y la desviación estándar diaria (std_log)
#    (Ambos sobre df_clean['Return_log'])

mean_log = df_clean['Return_log'].mean()
std_log = df_clean['Return_log'].std()

# C. Anualiza las métricas
N_DIAS = 252
mean_annual = mean_log * N_DIAS
vol_annual = std_log * np.sqrt(N_DIAS)

# D. Imprime los resultados
print(f"Media Diaria (Log): {mean_log:.6f}")
print(f"Volatilidad Diaria (Log): {std_log:.6f}")
print("---")
print(f"Retorno Anualizado (Log): {mean_annual:.4f}")
print(f"Volatilidad Anualizada: {vol_annual:.4f}")