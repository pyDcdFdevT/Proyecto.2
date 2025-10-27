# Archivo: Ejercicios/09.4_pandas_retornos.py

import pandas as pd
import numpy as np # ¡Añadido por necesidad!

data = {
    'Open': [100.0, 101.5, 99.8, 103.0, 102.5],
    'Close': [101.2, 99.5, 102.8, 102.1, 104.0]
}

df_precios = pd.DataFrame(data)

# 1. CALCULA EL RETORNO LOGARÍTMICO
df_precios['LogReturn'] = np.log(df_precios['Close'] / df_precios['Close'].shift(1))

# 2. Imprime el resultado (solo las columnas relevantes)
print("--- DATAFRAME CON RETORNOS LOGARÍTMICOS ---")
print(df_precios[['Close', 'LogReturn']])