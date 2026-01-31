import yfinance as yf
import pandas as pd

# --- PARÁMETROS DE ENTRADA ---
# Usamos constantes en mayúsculas para facilitar cambios rápidos de activos
TICKER = 'TSLA'

# --- OBTENCIÓN DE DATOS ---
df = yf.download(TICKER, period='1y')

# --- LIMPIEZA Y TRANSFORMACIÓN ---
# Extraemos el cierre y calculamos retornos. 
# El MultiIndex de yfinance requiere usar .xs para evitar errores de nivel.
cierre = df.xs('Close', axis=1, level='Price')
retornos = cierre.pct_change().dropna()

# --- ANÁLISIS ESTADÍSTICO ---
# Usamos .iloc[0] para obtener el valor numérico puro (float) y evitar conflictos de formato
volatilidad = retornos.std().iloc[0]

# --- RESULTADOS ---
print(f"Riesgo de {TICKER}: {volatilidad:.2%}")