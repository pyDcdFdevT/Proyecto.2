import yfinance as yf
import numpy as np

tickers = ['TSLA', 'KO', 'SPY', 'GLD']
data = yf.download(tickers, start='2020-01-01', progress=False)['Close']
                   
print(f"Datos descargados: {data.shape}")
print(f"Período: {data.index[0].date()} al {data.index[-1].date()}\n")

log_returns = np.log(data / data.shift(1))

matriz_corr = log_returns.corr()

print("="*50)
print("📊MATRIZ DE CORRELACIÓN (2020-actualidad)")
print("="*50)
print(matriz_corr)

# TESLA y COCA-COLA tienen correlación BAJÍSIMA (0.14)
# Esto es un SUPER PODER para inversores:

print("💡 INSIGHT CLAVE:")
print("Si combinas Tesla (loquito) con Coca-Cola (tranquilo)")
print("Tienes un portafolio que NO se cae todo a la vez")
print("Cuando Tesla cae -20%, Coca-Cola probablemente solo -3%")

print("🛡️ EL ORO ES TU SEGURO:")
print("Correlación 0.07 con Tesla = CASI CERO")
print("Cuando acciones se derrumban, el oro muchas veces SUBE")
print("Por eso se llama 'activo refugio'")


#===============================================================================#
# Piensa en parejas bailando:
#- Correlación 1.0 = Bailan perfectamente juntos (siempre igual)
#- Correlación 0.5 = Bailan parecido, pero no siempre igual  
#- Correlación 0.0 = Cada uno baila su rollo (no se coordinan)
#- Correlación -1.0 = Cuando uno va arriba, el otro va abajo (opuestos)

#===============================================================================#

#1. ORO vs ACCIONES (0.07 a 0.13):
# "El oro baila su propia música, le importa un pepino lo que hagan las acciones"
   
#2. TESLA vs COCA-COLA (0.14):
# "Tesla y Coca-Cola van cada uno por su lado, casi no se hablan"
   
#3. COCA-COLA vs MERCADO (0.56):
# "Coca-Cola sigue al mercado, pero con su propio ritmo lento"
   
#4. TESLA vs MERCADO (0.54):
# "Tesla sigue al mercado... a veces, cuando le da la gana"

#===============================================================================#