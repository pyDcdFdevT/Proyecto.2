# Tu código es correcto, pero sugiero:
import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['TSLA', 'KO']

# Mejor práctica: separar descarga de procesamiento
data = yf.download(tickers, start='2020-01-01', progress=False)['Close']

# Verificar que tenemos datos
print(f"Datos descargados: {data.shape}")
print(f"Período: {data.index[0].date()} al {data.index[-1].date()}")

# Cálculo de retornos logarítmicos (correcto)
log_returns = np.log(data / data.shift(1))

# Volatilidad anualizada
vol_anualizada = log_returns.std() * np.sqrt(252)

print("\n" + "="*50)
print("📊 VOLATILIDAD ANUALIZADA (2020-actualidad)")
print("="*50)
for ticker in tickers:
    print(f"{ticker}: {vol_anualizada[ticker]:.2%}")