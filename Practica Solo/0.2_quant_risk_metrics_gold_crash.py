import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Configuración
tickers = ['AAPL', 'TSLA', 'GLD', 'XLU']
datos = yf.download(tickers, period='1y') # Bajamos 1 año para tener perspectiva histórica
cierre = datos['Close']

# 2. Cálculo de Retornos y Volatilidad Rodante (ventana de 20 días)
retornos = cierre.pct_change().dropna()
# La volatilidad anualizada (std * raíz de 252 días hábiles)
vol_rodante = retornos.rolling(window=20).std() * np.sqrt(252)

# 3. Cálculo de Max Drawdown (La joya de la corona)
# Fórmula: (Precio Actual / Máximo Histórico hasta hoy) - 1
picos = cierre.cummax()
drawdowns = (cierre / picos) - 1
max_drawdown = drawdowns.min()

# 4. Resultados en Terminal
print("--- MÉTRICAS DE RIESGO AVANZADAS ---")
print("\nMAX DRAWDOWN (Peor caída desde el pico):")
print(max_drawdown)

print("\n--- VOLATILIDAD ANUALIZADA ÚLTIMOS 5 DÍAS ---")
print(vol_rodante.tail())

# 5. Visualización del "Dolor" (Drawdown)
drawdowns.plot(figsize=(12, 6))
plt.title("Curva de Drawdown: ¿Cuánto hemos perdido desde el pico?")
plt.axhline(0, color='black', lw=1)
plt.fill_between(drawdowns.index, drawdowns['GLD'], color='gold', alpha=0.3, label='Drawdown Oro')
plt.legend()
plt.show()

# Calculamos la matriz de correlación de los retornos
matriz_corr = retornos.corr()

print("\n--- MATRIZ DE CORRELACIÓN (Último año) ---")
print(matriz_corr)

# Últimos 5 Días 

corr_caos = retornos.tail(5).corr()
print("\n--- CORRELACIÓN EN EL 'CAOS' (Últimos 5 días)")
print(corr_caos)