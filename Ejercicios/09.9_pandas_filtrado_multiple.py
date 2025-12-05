import pandas as pd
import numpy as np

# Datos de ejemplo (precios de cierre)
data = {'Close': [100.0, 101.5, 99.8, 103.0, 102.1]}
df = pd.DataFrame(data)

# 1. CALCULAR LOG-RETURN
df['LogReturn'] = np.log(df['Close'] / df['Close'].shift(1))

# -----------------------------------------------------
# TU CÓDIGO AQUÍ
# -----------------------------------------------------

# 2. Define las dos condiciones booleanas.
#    Cierre > 101.5 (Condicion 1)
#    LogReturn > 0 (Condicion 2)

condicion_1 = df['Close'] > 101.5
condicion_2 = df['LogReturn'] > 0


# 3. Combina las condiciones usando el operador booleano & (AND) para crear df_filtrado.
#    Pista: df[ (condicion_1) & (condicion_2) ]

df_filtrado = df[(condicion_1) & (condicion_2)]


# 4. Imprime el DataFrame Filtrado
print("--- Días de Cierre Alto Y Ganancia (Cierre > 101.5 & LogReturn > 0) ---")
print(df_filtrado)