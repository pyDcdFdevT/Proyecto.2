import yfinance as yf
import pandas as pd


tickers = ['AAPL', 'TSLA', 'GLD', 'XLU']
datos = yf.download(tickers, period='1mo')

print("--- PRIMERAS FILAS ---")
print(datos.head())

cierre = datos['Close']
retornos = cierre.pct_change()
retornos_limpios = retornos.dropna()

print("--- RETORNOS DIARIOS ---")
print(retornos.head())

print(retornos_limpios.describe())

print("--- RESUMEN ESTADÍSTICO (VOLATILIDAD) ---")
print(retornos_limpios.describe())

dia_negro = retornos_limpios[retornos_limpios['GLD'] < -0.05]
print("--- DÍA DE CAÍDA MASIVA EN ORO ---")
print(dia_negro['GLD'])

import matplotlib.pyplot as plt 
retornos_limpios.plot(figsize=(12, 6))
plt.axhline(0, color='black', lw=1, linestyle='--')
plt.title("Impacto del 'Efecto Warsh' en el mercado - 30/01/2026")
plt.ylabel("Retorno Diario (Decimal)")
plt.xlabel("Fecha")
plt.grid(True, alpha=0.3)
plt.show()