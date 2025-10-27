import pandas as pd
import numpy as np

# Datos simulados de precios de cierre para dos acciones (AAPL y MSFT)
data = {
    'AAPL_Close': [150.0, 152.5, 151.0, 154.5, 153.0],
    'MSFT_Close': [280.0, 283.0, 279.5, 285.0, 282.5]
}

df_acciones = pd.DataFrame(data)

# 1. Calcule el PRECIO MEDIO de CIERRE de MSFT.
#    Asigne el resultado a la variable 'media_msft'.
#    Pista: df_acciones[...]

media_msft = df_acciones['MSFT_Close'].mean()


# 2. Calcule la VOLATILIDAD (Desviación Estándar) de AAPL.
#    Asigne el resultado a la variable 'volatilidad_aapl'.
#    Pista: df_acciones[...]

volatilidad_aapl = df_acciones['AAPL_Close'].std()


# 3. Imprima ambos resultados con dos decimales de precisión.
print(f"Precio Medio de MSFT: {media_msft:.2f}")
print(f"Volatilidad de AAPL: {volatilidad_aapl:.2f}")