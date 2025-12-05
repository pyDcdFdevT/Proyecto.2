# 🚀 CHEAT SHEET - Análisis Financiero con Python

## 📥 DESCARGAR DATOS
```python
import yfinance as yf
datos = yf.download('TICKER', start='YYYY-MM-DD', progress=False)['Close']

🔄 TRANSFORMACIONES COMUNES

Retornos simples: .pct_change()
Retornos log: np.log(precio / precio.shift(1))
Media móvil simple: .rolling(N).mean()
Media móvil exponencial: .ewm(span=N, adjust=False).mean()
Volatilidad anualizada: retornos.std() * np.sqrt(252)
📊 ESTADÍSTICAS

Promedio: .mean()
Desviación estándar: .std()
Skewness (asimetría): .skew()
Kurtosis (colas pesadas): .kurtosis()
Correlación: .corr()