import pandas as pd
import numpy as np

# Datos simulados de precios de cierre (los mismos que antes)
data = {'Close': [100.0, 101.5, 99.8, 103.0, 102.1]}
df = pd.DataFrame(data)

# -----------------------------------------------------
# TU CÓDIGO AQUÍ (Usa df original)
# -----------------------------------------------------

# 1. Imprime las estadísticas descriptivas de la columna 'Close'.
#    Pista de la chuleta (Sección 4): df['Columna'].describe()
print("--- 1. Estadísticas Descriptivas ---")
df['Close'].describe()

# 2. Asigna una lista de fechas como nuevo índice del DataFrame.
#    El índice debe ser un objeto de tiempo (DatetimeIndex).
#    Pista: df.index = pd.to_datetime(...)

fechas = ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-06', '2025-01-07']
df.index = pd.to_datetime(fechas)
# 3. Imprime el DataFrame y la confirmación del tipo de índice.
print("\n--- 2. DataFrame con Índice de Tiempo ---")
print(df['Close'].describe())
print("\nTipo de índice:", type(df.index))