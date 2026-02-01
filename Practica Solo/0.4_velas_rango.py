import yfinance as yf
import pandas as pd

# ---- PARAMETROS ----
TICKER = 'TSLA'

# --- OBTENCIÓN DE DATOS ---
df = yf.download(TICKER, period='1y')

# --- TRANSFORMACIÓN ---
df['Rango_Diario'] = df['High'] - df['Low']

# 1. Aplanamos las columnas para que High y Low sean columnas simples
precios = df.xs(TICKER, axis=1, level='Ticker')

# 2. Ahora usamos 'precios' en lugar de 'df'
precios['Rango_Diario'] = precios['High'] - precios['Low']
media_rango = precios['Rango_Diario'].mean()

media_rango = df['Rango_Diario'].mean()

print(f"Rango intradía promedio de {TICKER}: {media_rango:.2f} USD")

precios['Cuerpo'] = precios['Close'] - precios['Open']
# Saca la media del cuerpo absoluto (usando .abs() porque puede ser negativo)
media_cuerpo = precios['Cuerpo'].abs().mean()

print(f"Cuerpo promedio: {media_cuerpo:2f} USD")