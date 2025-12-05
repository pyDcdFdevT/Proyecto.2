"""
===================================================
PLANTILLA: Análisis de Volatilidad y Riesgo
Autor: [Tu Nombre]
Fecha: [Fecha]
Versión: 1.0
===================================================
DESCRIPCIÓN: Template para análisis avanzado de volatilidad y métricas de riesgo
USO: Modificar ticker y parámetros según necesidad
===================================================
"""

# ============================================================================
# 1. IMPORTS
# ============================================================================
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, t, skew, kurtosis
import warnings
warnings.filterwarnings('ignore')

# Configuración visual
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("viridis")

# ============================================================================
# 2. CONFIGURACIÓN (MODIFICAR ESTO)
# ============================================================================
TICKER = 'SPY'                    # Activo a analizar
START_DATE = '2020-01-01'        # Fecha de inicio
END_DATE = None                   # None = hasta hoy

# PARÁMETROS DE ANÁLISIS
PERIODO_VOLATILIDAD = 30          # Días para volatilidad móvil
CONFIANZA_VaR = 0.95              # Nivel de confianza para Value at Risk (95%)
HORIZONTE_VaR = 1                 # Días para el horizonte del VaR
PERIODO_ROLLING = 252             # Días para cálculos rolling (1 año trading)

# ============================================================================
# 3. FUNCIONES DE CÁLCULO DE RIESGO
# ============================================================================
def calcular_retornos(precios):
    """Calcula retornos logarítmicos"""
    return np.log(precios / precios.shift(1)).dropna()

def volatilidad_historica(retornos, window=PERIODO_VOLATILIDAD):
    """Calcula volatilidad histórica móvil"""
    return retornos.rolling(window=window).std() * np.sqrt(252)

def calcular_var_historico(retornos, confianza=CONFIANZA_VaR):
    """Value at Risk por método histórico"""
    return np.percentile(retornos, (1 - confianza) * 100)

def calcular_var_paramétrico(retornos, confianza=CONFIANZA_VaR):
    """Value at Risk asumiendo distribución normal"""
    media = retornos.mean()
    desviacion = retornos.std()
    z_score = norm.ppf(1 - confianza)
    return media + z_score * desviacion

def calcular_expected_shortfall(retornos, confianza=CONFIANZA_VaR):
    """Expected Shortfall (CVaR) - Pérdida promedio en el peor % de casos"""
    var = calcular_var_historico(retornos, confianza)
    return retornos[retornos <= var].mean()

def calcular_max_drawdown(precios):
    """Calcula el máximo drawdown (máxima caída desde pico)"""
    rolling_max = precios.expanding().max()
    drawdown = (precios - rolling_max) / rolling_max
    return drawdown.min()

def calcular_sharpe_ratio(retornos, riesgo_libre=0.02):
    """Ratio de Sharpe (retorno ajustado por riesgo)"""
    retorno_anual = retornos.mean() * 252
    volatilidad_anual = retornos.std() * np.sqrt(252)
    return (retorno_anual - riesgo_libre) / volatilidad_anual

def calcular_sortino_ratio(retornos, riesgo_libre=0.02):
    """Ratio de Sortino (solo penaliza volatilidad negativa)"""
    retorno_anual = retornos.mean() * 252
    downside_returns = retornos[retornos < 0]
    downside_dev = downside_returns.std() * np.sqrt(252) if len(downside_returns) > 0 else 0
    return (retorno_anual - riesgo_libre) / downside_dev if downside_dev != 0 else np.nan

# ============================================================================
# 4. ANÁLISIS DE DISTRIBUCIÓN
# ============================================================================
def analizar_distribucion(retornos):
    """Analiza propiedades estadísticas de la distribución de retornos"""
    
    # Estadísticas básicas
    skewness = skew(retornos)
    kurt = kurtosis(retornos, fisher=True)  # Fisher: normal = 0
    
    # Test de normalidad visual (QQ-Plot)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # 1. Histograma vs Normal
    axes[0].hist(retornos, bins=50, density=True, alpha=0.7, label='Retornos')
    x = np.linspace(retornos.min(), retornos.max(), 100)
    axes[0].plot(x, norm.pdf(x, retornos.mean(), retornos.std()), 
                'r-', lw=2, label='Normal', alpha=0.8)
    axes[0].set_title('Distribución de Retornos', fontsize=12)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 2. QQ-Plot
    from scipy.stats import probplot
    probplot(retornos, dist="norm", plot=axes[1])
    axes[1].set_title('QQ-Plot vs Distribución Normal', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    
    # 3. Box plot para outliers
    axes[2].boxplot(retornos, vert=True, patch_artist=True)
    axes[2].set_title('Box Plot - Detección de Outliers', fontsize=12)
    axes[2].set_ylabel('Retorno Diario')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analisis_distribucion.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return {
        'skewness': skewness,
        'kurtosis': kurt,
        'es_normal': abs(skewness) < 0.5 and abs(kurt) < 1,  # Regla empírica
        'outliers': len(retornos[np.abs(retornos) > 3 * retornos.std()])
    }

# ============================================================================
# 5. VISUALIZACIONES DE RIESGO
# ============================================================================
def crear_visualizaciones_riesgo(precios, retornos, resultados):
    """Genera gráficos para análisis de riesgo"""
    
    # 5.1. PRECIO Y VOLATILIDAD MÓVIL
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    
    # Gráfico de precios
    axes[0].plot(precios.index, precios, label='Precio', linewidth=2, alpha=0.8)
    axes[0].set_ylabel('Precio (USD)', fontsize=12)
    axes[0].set_title(f'{TICKER} - Análisis de Precio y Volatilidad', fontsize=14)
    axes[0].legend(loc='upper left')
    axes[0].grid(True, alpha=0.3)
    
    # Gráfico de volatilidad móvil
    volatilidad = volatilidad_historica(retornos)
    axes[1].plot(volatilidad.index, volatilidad, 
                label=f'Volatilidad {PERIODO_VOLATILIDAD}d', 
                color='red', linewidth=2, alpha=0.8)
    axes[1].axhline(y=volatilidad.mean(), color='green', 
                   linestyle='--', alpha=0.7, label='Media')
    axes[1].fill_between(volatilidad.index, 0, volatilidad, 
                        alpha=0.3, color='red')
    axes[1].set_ylabel('Volatilidad Anualizada', fontsize=12)
    axes[1].set_xlabel('Fecha', fontsize=12)
    axes[1].legend(loc='upper left')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('precio_volatilidad.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 5.2. DRAWDOWN
    plt.figure(figsize=(12, 4))
    rolling_max = precios.expanding().max()
    drawdown_series = (precios - rolling_max) / rolling_max
    
    plt.fill_between(drawdown_series.index, drawdown_series, 0, 
                    where=drawdown_series < 0, 
                    color='red', alpha=0.5, label='Drawdown')
    plt.axhline(y=resultados['max_drawdown'], color='darkred', 
               linestyle='--', label=f"Máx: {resultados['max_drawdown']:.1%}")
    plt.title('Historial de Drawdown', fontsize=14)
    plt.ylabel('Drawdown', fontsize=12)
    plt.xlabel('Fecha', fontsize=12)
    plt.legend(loc='lower left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('drawdown_history.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 5.3. DISTRIBUCIÓN DE PÉRDIDAS (Para VaR)
    plt.figure(figsize=(10, 6))
    
    # Histograma de retornos negativos
    retornos_negativos = retornos[retornos < 0]
    plt.hist(retornos_negativos, bins=30, density=True, 
            alpha=0.7, color='red', label='Retornos Negativos')
    
    # Líneas de VaR
    var_hist = resultados['var_historico']
    var_param = resultados['var_paramétrico']
    es = resultados['expected_shortfall']
    
    plt.axvline(x=var_hist, color='darkred', linestyle='-', 
               linewidth=2, label=f'VaR Histórico ({CONFIANZA_VaR:.0%})')
    plt.axvline(x=var_param, color='orange', linestyle='--', 
               linewidth=2, label=f'VaR Paramétrico ({CONFIANZA_VaR:.0%})')
    plt.axvline(x=es, color='purple', linestyle=':', 
               linewidth=2, label=f'Expected Shortfall ({CONFIANZA_VaR:.0%})')
    
    plt.title('Distribución de Pérdidas y Métricas de Riesgo', fontsize=14)
    plt.xlabel('Retorno Diario', fontsize=12)
    plt.ylabel('Densidad', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('distribucion_perdidas_var.png', dpi=150, bbox_inches='tight')
    plt.show()

# ============================================================================
# 6. EJECUCIÓN PRINCIPAL
# ============================================================================
if __name__ == "__main__":
    print("="*70)
    print("📉 ANÁLISIS DE VOLATILIDAD Y RIESGO")
    print("="*70)
    
    # 6.1. Descargar datos
    print(f"📥 Descargando datos para {TICKER}...")
    data = yf.download(TICKER, start=START_DATE, end=END_DATE, progress=False)['Close']
    df = pd.DataFrame(data)
    df.columns = ['Close']
    
    if df.empty:
        print(f"❌ No se pudieron descargar datos para {TICKER}")
    else:
        print(f"✅ Datos descargados: {df.shape[0]} días desde {df.index[0].date()}")
        
        # 6.2. Calcular retornos
        retornos = calcular_retornos(df['Close'])
        
        # 6.3. Calcular todas las métricas de riesgo
        print("\n📊 Calculando métricas de riesgo...")
        
        resultados = {
            'precio_actual': df['Close'].iloc[-1],
            'retorno_promedio_diario': retornos.mean(),
            'retorno_anualizado': retornos.mean() * 252,
            'volatilidad_anualizada': retornos.std() * np.sqrt(252),
            'volatilidad_promedio_30d': volatilidad_historica(retornos).mean(),
            'var_historico': calcular_var_historico(retornos),
            'var_paramétrico': calcular_var_paramétrico(retornos),
            'expected_shortfall': calcular_expected_shortfall(retornos),
            'max_drawdown': calcular_max_drawdown(df['Close']),
            'sharpe_ratio': calcular_sharpe_ratio(retornos),
            'sortino_ratio': calcular_sortino_ratio(retornos),
        }
        
        # 6.4. Análisis de distribución
        print("📈 Analizando distribución de retornos...")
        distribucion = analizar_distribucion(retornos)
        resultados.update(distribucion)
        
        # 6.5. Mostrar resultados en consola
        print("\n" + "="*70)
        print("📋 RESUMEN DE MÉTRICAS DE RIESGO")
        print("="*70)
        
        print(f"\n📈 RENDIMIENTO:")
        print(f"  Precio actual: ${resultados['precio_actual']:.2f}")
        print(f"  Retorno diario promedio: {resultados['retorno_promedio_diario']:.4%}")
        print(f"  Retorno anualizado: {resultados['retorno_anualizado']:.2%}")
        
        print(f"\n📉 VOLATILIDAD:")
        print(f"  Volatilidad anualizada: {resultados['volatilidad_anualizada']:.2%}")
        print(f"  Volatilidad promedio (30d móvil): {resultados['volatilidad_promedio_30d']:.2%}")
        
        print(f"\n🎯 MÉTRICAS DE RIESGO:")
        print(f"  Máximo Drawdown: {resultados['max_drawdown']:.2%}")
        print(f"  Value at Risk (Histórico, {CONFIANZA_VaR:.0%}): {resultados['var_historico']:.4%}")
        print(f"  Value at Risk (Paramétrico, {CONFIANZA_VaR:.0%}): {resultados['var_paramétrico']:.4%}")
        print(f"  Expected Shortfall ({CONFIANZA_VaR:.0%}): {resultados['expected_shortfall']:.4%}")
        
        print(f"\n⭐ RATIOS DE PERFORMANCE:")
        print(f"  Sharpe Ratio: {resultados['sharpe_ratio']:.3f}")
        print(f"  Sortino Ratio: {resultados['sortino_ratio']:.3f}")
        
        print(f"\n📊 PROPIEDADES ESTADÍSTICAS:")
        print(f"  Skewness: {resultados['skewness']:.3f} {'(positiva)' if resultados['skewness'] > 0 else '(negativa)'}")
        print(f"  Kurtosis: {resultados['kurtosis']:.3f} {'(colas pesadas)' if resultados['kurtosis'] > 0 else '(colas ligeras)'}")
        print(f"  Outliers (>3σ): {resultados['outliers']} eventos")
        print(f"  ¿Distribución normal?: {'SÍ' if resultados['es_normal'] else 'NO'}")
        
        print(f"\n📅 CONTEXTO:")
        print(f"  Período analizado: {df.shape[0]} días")
        print(f"  Desde: {df.index[0].date()}")
        print(f"  Hasta: {df.index[-1].date()}")
        
        # 6.6. Interpretación guiada
        print("\n" + "="*70)
        print("💡 INTERPRETACIÓN PARA TOMA DE DECISIONES")
        print("="*70)
        
        vol_cat = "ALTA" if resultados['volatilidad_anualizada'] > 0.3 else "MODERADA" if resultados['volatilidad_anualizada'] > 0.15 else "BAJA"
        print(f"\n1. NIVEL DE RIESGO: {vol_cat}")
        print(f"   {TICKER} tiene volatilidad {vol_cat.lower()} ({resultados['volatilidad_anualizada']:.1%} anual)")
        
        print(f"\n2. PEOR ESCENARIO HISTÓRICO:")
        print(f"   En un día normal, con {CONFIANZA_VaR:.0%} confianza, no perderás más de {abs(resultados['var_historico']):.2%}")
        print(f"   En el peor {100*(1-CONFIANZA_VaR):.0f}% de días, perderás en promedio {abs(resultados['expected_shortfall']):.2%}")
        
        print(f"\n3. RECOMENDACIÓN BASADA EN RATIOS:")
        if resultados['sharpe_ratio'] > 1:
            print("   ✅ Sharpe Ratio > 1: Buen retorno ajustado por riesgo")
        else:
            print("   ⚠️  Sharpe Ratio < 1: Retorno podría no compensar el riesgo")
        
        if resultados['sortino_ratio'] > resultados['sharpe_ratio']:
            print("   ✅ Sortino > Sharpe: La volatilidad proviene más de ganancias que de pérdidas")
        
        # 6.7. Generar visualizaciones
        print("\n" + "="*70)
        print("📊 GENERANDO VISUALIZACIONES")
        print("="*70)
        
        crear_visualizaciones_riesgo(df['Close'], retornos, resultados)
        
        print("\n✅ Análisis completado. Gráficos guardados como:")
        print("   - analisis_distribucion.png")
        print("   - precio_volatilidad.png")
        print("   - drawdown_history.png")
        print("   - distribucion_perdidas_var.png")
        
        print("\n" + "="*70)
        print("🎯 USO PRÁCTICO DE ESTE ANÁLISIS:")
        print("="*70)
        print("1. DIVERSIFICAR si volatilidad es muy alta")
        print("2. USAR STOP LOSS basado en VaR histórico")
        print("3. MONITOREAR drawdown para timing de entrada/salida")
        print("4. COMPARAR ratios con otros activos para asignación")