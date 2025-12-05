import yfinance as yf
import pandas as pd

ticker = 'SPY'
PERIODO = 50   
data = yf.download(ticker, start='2020-01-01', progress=False)['Close']
df = pd.DataFrame(data)
df.columns = ['Close']

df['SMA_50'] = df['Close'].rolling(PERIODO).mean()

df['EMA_50'] = df['Close'].ewm(span=PERIODO, adjust=False).mean()

print('='*50)
print("--- Últimos 5 Días del Consenso de Precio ---")
print('='*50)
print(df.tail())