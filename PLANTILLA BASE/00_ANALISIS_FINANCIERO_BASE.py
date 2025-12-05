"""
==============================================
PLANTILLA BASE: Análisis Financiero con Python
Autor: [Tu Nombre]
Fecha: [Fecha]
Versión: 1.0
==============================================
DESCRIPCIÓN: Template para análisis cuantitativo básico
USO: Copiar y modificar según necesidades específicas
==============================================
"""

# ============================================================================
# 1. IMPORTS BÁSICOS (Herramientas esenciales)
# ============================================================================
import yfinance as yf          # Descarga datos financieros
import pandas as pd            # Manipulación de datos (tablas)
import numpy as np             # Cálculos numéricos
import matplotlib.pyplot as plt # Gráficos básicos
# import seaborn as sns        # Gráficos avanzados (descomentar si necesitas)

# ============================================================================
# 2. CONFIGURACIÓN INICIAL (Modificar estos valores)
# ============================================================================
TICKER = 'SPY'                 # Símbolo del activo (ej: 'AAPL', 'TSLA', 'BTC-USD')
START_DATE = '2020-01-01'      # Fecha de inicio (formato: 'YYYY-MM-DD')
END_DATE = None                # Fecha de fin (None = hasta hoy)
PERIODO = 50                   # Para medias móviles, volatilidad, etc.

# ============================================================================
# 3. OBTENCIÓN DE DATOS
# ============================================================================
def descargar_datos(ticker=TICKER, inicio=START_DATE, fin=END_DATE):
    """
    Descarga precios de cierre desde Yahoo Finance
    """
    datos = yf.download(
        ticker, 
        start=inicio, 
        end=fin, 
        progress=False
    )['Close']
    
    df = pd.DataFrame(datos)
    df.columns = ['Close']
    return df

# Ejecutar descarga
df = descargar_datos()
print(f"✓ Datos descargados: {df.shape[0]} días desde {df.index[0].date()}")

# ============================================================================
# 4. TRANSFORMACIONES COMUNES (Elegir las necesarias)
# ============================================================================
# A) RETORNOS
df['Returns_Simple'] = df['Close'].pct_change()            # Retornos simples
df['Returns_Log'] = np.log(df['Close'] / df['Close'].shift(1))  # Retornos logarítmicos

# B) MEDIAS MÓVILES
df[f'SMA_{PERIODO}'] = df['Close'].rolling(PERIODO).mean()      # Media Simple
df[f'EMA_{PERIODO}'] = df['Close'].ewm(span=PERIODO, adjust=False).mean()  # Media Exponencial

# C) VOLATILIDAD (descomentar si necesitas)
# df['Volatility_30d'] = df['Returns_Log'].rolling(30).std() * np.sqrt(252)

# ============================================================================
# 5. ESTADÍSTICAS BÁSICAS
# ============================================================================
def calcular_estadisticas(dataframe):
    """Calcula métricas estadísticas básicas"""
    stats = {
        'Precio_Actual': dataframe['Close'].iloc[-1],
        'Media_30d': dataframe['Close'].tail(30).mean(),
        'Volatilidad_Anual': dataframe['Returns_Log'].std() * np.sqrt(252),
        'Skewness': dataframe['Returns_Log'].skew(),
        'Kurtosis': dataframe['Returns_Log'].kurtosis(),
        'Max_Drawdown': (dataframe['Close'] / dataframe['Close'].cummax() - 1).min()
    }
    return stats

estadisticas = calcular_estadisticas(df)

# ============================================================================
# 6. VISUALIZACIÓN BÁSICA (descomentar para usar)
# ============================================================================
"""
# Gráfico de precios y media móvil
plt.figure(figsize=(12, 6))
plt.plot(df['Close'][-100:], label='Precio', alpha=0.7)
plt.plot(df[f'SMA_{PERIODO}'][-100:], label=f'SMA {PERIODO}', linewidth=2)
plt.title(f'{TICKER} - Precio y Media Móvil')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
"""

# ============================================================================
# 7. RESULTADOS EN CONSOLA
# ============================================================================
print("\n" + "="*60)
print(f"📊 ANÁLISIS BÁSICO: {TICKER}")
print("="*60)

print(f"\n📈 PRECIOS:")
print(f"  Último precio: ${estadisticas['Precio_Actual']:.2f}")
print(f"  Media 30 días: ${estadisticas['Media_30d']:.2f}")

print(f"\n📊 ESTADÍSTICAS DE RETORNO:")
print(f"  Volatilidad anualizada: {estadisticas['Volatilidad_Anual']:.2%}")
print(f"  Skewness (asimetría): {estadisticas['Skewness']:.4f}")
print(f"  Kurtosis (colas): {estadisticas['Kurtosis']:.4f}")
print(f"  Máximo Drawdown: {estadisticas['Max_Drawdown']:.2%}")

print(f"\n📅 PERIODO ANALIZADO:")
print(f"  Desde: {df.index[0].date()}")
print(f"  Hasta: {df.index[-1].date()}")
print(f"  Total días: {df.shape[0]}")

print("\n" + "="*60)
print("✅ Plantilla ejecutada correctamente")
print("="*60)

# ============================================================================
# 8. GUARDAR RESULTADOS (opcional)
# ============================================================================
# df.to_csv(f'resultados_{TICKER}.csv')
# print(f"\n💾 Datos guardados en: resultados_{TICKER}.csv")