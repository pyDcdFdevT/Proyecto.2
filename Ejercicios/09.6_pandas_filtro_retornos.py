import pandas as pd
import numpy as np

data = {
    'Close': [100.0, 101.5, 99.8, 103.0, 102.1]
}

df_precios = pd.DataFrame(data)

df_precios['Return'] = df_precios['Close'].pct_change()

df_ganancias = df_precios[df_precios['Return'] > 0]

print("--- Días de Ganancia (Retorno > 0) ---")
print(df_ganancias)
