import yfinance as yf
import pandas as pd

# --- CONFIGURACIÓN (Materia Prima) ---
TICKER = 'TSLA'  # Puedes cambiarlo por 'BTC-USD', 'AAPL' o 'NVDA'
FECHA_INICIO = '2025-01-01'
FECHA_FIN = '2025-12-31'

# 1. DESCARGA
# Descargamos como string para manejar una estructura más limpia
df = yf.download(TICKER, start=FECHA_INICIO, end=FECHA_FIN)

print(f"--- PRIMERAS FILAS DE {TICKER} ---")
print(df.head())

# 2. PROCESO (Lógica de Flujo)
# Usamos .xs para entrar al edificio y sacar solo la columna 'Close' 
# Esto "aplana" el MultiIndex y nos deja una Serie simple.
cierre = df.xs('Close', axis=1, level='Price')

# Ahora calculamos retornos. Como 'cierre' tiene el nombre del ticker arriba, 
# 'retornos' también lo tendrá.
retornos = cierre.pct_change().dropna()

# 3. CÁLCULO ESTADÍSTICO
# Al ser una Serie, .mean() nos daría otra serie. 
# Usamos .iloc[0] para extraer el NÚMERO puro y que el print no falle.
media = retornos.mean().iloc[0]
volatilidad = retornos.std().iloc[0]

# 4. OUTPUT (Visualización de resultados)
print(f"\n" + "="*30)
print(f"ANÁLISIS DE RIESGO: {TICKER}")
print(f"="*30)
print(f"Retorno promedio diario: {media:.4f} ({media*100:.2f}%)")
print(f"Volatilidad diaria:      {volatilidad:.4f} ({volatilidad*100:.2f}%)")
print(f"="*30)

# Nota: La volatilidad anualizada es la diaria * raíz de 252 días hábiles
vol_anual = volatilidad * (252**0.5)
print(f"Volatilidad Anualizada:  {vol_anual:.2f} ({vol_anual*100:.2f}%)")