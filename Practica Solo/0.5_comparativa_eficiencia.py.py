import yfinance as yf
import pandas as pd

# --- PARÁMETROS ---
# Una lista de activos con personalidades distintas

ACTIVOS = ['TSLA', 'KO', 'BTC-USD', 'GLD', 'AAPL']
FECHA = '2025-01-01'

print("-- INICIANDO ESCÁNER DE EFICIENCIA ---")

for ticker in ACTIVOS:
    # 1. Descargamos los datos
    df= yf.download(ticker, start= FECHA, progress=False)
    # 2. Aplanado “Entramos en la "caja" de cada ticker
    datos = df.xs(ticker, axis= 1, level='Ticker')
    
    # 3. Cálculos
    rango = (datos['High'] - datos['Low']).mean()
    cuerpo = (datos['Close'] - datos['Open']).abs().mean()
    
    eficiencia = (cuerpo / rango) * 100
    
    # 4. Output
    print(f"\nActivo: {ticker}")
    print(f"    > Rango Promedio:   {rango:.2f} USD")
    print(f"    > Cuerpo Promedio:  {cuerpo:.2f} USD")
    print(f"    > EFICIENCIA:       {eficiencia:.2f}%")