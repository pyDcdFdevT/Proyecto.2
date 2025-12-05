"""
=================================================
PLANTILLA: Análisis de Correlación entre Activos
Autor: [Tu Nombre]
Fecha: [Fecha]
Versión: 1.0
=================================================
DESCRIPCIÓN: Template para analizar relaciones entre múltiples activos
USO: Modificar tickers y parámetros según necesidad
=================================================
"""

# ============================================================================
# 1. IMPORTS
# ============================================================================
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # Para tests estadísticos

# Configurar estilo visual
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# 2. CONFIGURACIÓN (MODIFICAR ESTO)
# ============================================================================
# LISTA DE ACTIVOS A ANALIZAR
TICKERS = ['SPY', 'QQQ', 'TLT', 'GLD', 'BTC-USD']  # Ejemplo: S&P500, Nasdaq, Bonos, Oro, Bitcoin
START_DATE = '2020-01-01'
END_DATE = None  # None = hasta hoy

# PERÍODOS PARA ANÁLISIS (puedes modificarlos)
PERIODOS_CRISIS = {
    'COVID_2020': ('2020-02-01', '2020-06-01'),
    'INFLACION_2022': ('2022-01-01', '2022-12-31'),
    'NORMAL_2023': ('2023-01-01', '2023-12-31')
}

# ============================================================================
# 3. FUNCIÓN PARA DESCARGAR DATOS
# ============================================================================
def descargar_datos_multiactivos(tickers, inicio, fin):
    """Descarga precios de múltiples activos"""
    print(f"📥 Descargando datos para {len(tickers)} activos...")
    
    datos = yf.download(
        tickers,
        start=inicio,
        end=fin,
        progress=False,
        group_by='ticker'
    )
    
    # Extraer precios de cierre de cada activo
    precios = pd.DataFrame()
    for ticker in tickers:
        if ticker in datos.columns.get_level_values(0):
            precios[ticker] = datos[(ticker, 'Close')]
        else:
            print(f"⚠️  {ticker} no disponible, saltando...")
    
    print(f"✅ Datos descargados: {precios.shape[0]} días para {precios.shape[1]} activos")
    return precios.dropna()

# ============================================================================
# 4. CÁLCULO DE CORRELACIONES
# ============================================================================
def analizar_correlaciones(precios):
    """Calcula matriz de correlación y métricas relacionadas"""
    
    # Calcular retornos logarítmicos diarios
    retornos = np.log(precios / precios.shift(1)).dropna()
    
    # Matriz de correlación
    matriz_corr = retornos.corr()
    
    # Correlación promedio de cada activo con los demás
    corr_promedio = (matriz_corr.sum(axis=1) - 1) / (len(TICKERS) - 1)
    
    # Pares con mayor y menor correlación
    matriz_sin_diag = matriz_corr.copy()
    np.fill_diagonal(matriz_sin_diag.values, np.nan)
    
    max_corr = matriz_sin_diag.stack().idxmax()
    min_corr = matriz_sin_diag.stack().idxmin()
    
    return {
        'precios': precios,
        'retornos': retornos,
        'matriz_correlacion': matriz_corr,
        'correlacion_promedio': corr_promedio,
        'par_max_correlacion': max_corr,
        'par_min_correlacion': min_corr
    }

# ============================================================================
# 5. VISUALIZACIONES
# ============================================================================
def crear_visualizaciones(resultados, tickers):
    """Genera gráficos para el análisis de correlación"""
    
    precios = resultados['precios']
    retornos = resultados['retornos']
    matriz_corr = resultados['matriz_correlacion']
    
    # 5.1. MATRIZ DE CORRELACIÓN (Heatmap)
    plt.figure(figsize=(10, 8))
    mask = np.triu(np.ones_like(matriz_corr, dtype=bool))  # Máscara para triángulo superior
    sns.heatmap(matriz_corr, mask=mask, annot=True, fmt='.2f', 
                cmap='RdBu_r', center=0, square=True,
                linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Matriz de Correlación entre Activos\n(Retornos Diarios)', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('correlacion_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 5.2. PRECIOS NORMALIZADOS (Comparación visual)
    plt.figure(figsize=(12, 6))
    precios_normalizados = (precios / precios.iloc[0] * 100)
    for ticker in tickers[:5]:  # Mostrar solo primeros 5 para claridad
        plt.plot(precios_normalizados.index, precios_normalizados[ticker], 
                label=ticker, linewidth=2, alpha=0.8)
    
    plt.title('Evolución de Activos (Base 100 = Inicio)', fontsize=14)
    plt.ylabel('Precio Normalizado (100 = inicio)', fontsize=12)
    plt.xlabel('Fecha', fontsize=12)
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('precios_normalizados.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # 5.3. SCATTER PLOTS (para pares seleccionados)
    if len(tickers) >= 2:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Par con mayor correlación
        par_max = resultados['par_max_correlacion']
        axes[0].scatter(retornos[par_max[0]], retornos[par_max[1]], alpha=0.5, s=20)
        axes[0].set_xlabel(f'Retornos {par_max[0]}', fontsize=11)
        axes[0].set_ylabel(f'Retornos {par_max[1]}', fontsize=11)
        axes[0].set_title(f'Mayor Correlación ({matriz_corr.loc[par_max[0], par_max[1]]:.3f})', fontsize=12)
        axes[0].grid(True, alpha=0.3)
        
        # Par con menor correlación
        par_min = resultados['par_min_correlacion']
        axes[1].scatter(retornos[par_min[0]], retornos[par_min[1]], alpha=0.5, s=20)
        axes[1].set_xlabel(f'Retornos {par_min[0]}', fontsize=11)
        axes[1].set_ylabel(f'Retornos {par_min[1]}', fontsize=11)
        axes[1].set_title(f'Menor Correlación ({matriz_corr.loc[par_min[0], par_min[1]]:.3f})', fontsize=12)
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('scatter_correlacion.png', dpi=150, bbox_inches='tight')
        plt.show()

# ============================================================================
# 6. ANÁLISIS POR PERÍODO (Crisis vs Normal)
# ============================================================================
def analisis_periodos_especificos(tickers, periodos_dict):
    """Analiza correlación en diferentes períodos históricos"""
    
    resultados_periodos = {}
    
    for nombre_periodo, (inicio, fin) in periodos_dict.items():
        print(f"\n📅 Analizando período: {nombre_periodo} ({inicio} a {fin})")
        
        precios_periodo = descargar_datos_multiactivos(tickers, inicio, fin)
        if not precios_periodo.empty and len(precios_periodo.columns) >= 2:
            resultados = analizar_correlaciones(precios_periodo)
            resultados_periodos[nombre_periodo] = {
                'matriz': resultados['matriz_correlacion'],
                'dias': len(precios_periodo),
                'activos': list(precios_periodo.columns)
            }
            
            # Mostrar correlación promedio del período
            corr_prom = resultados['correlacion_promedio'].mean()
            print(f"   Correlación promedio: {corr_prom:.3f}")
    
    return resultados_periodos

# ============================================================================
# 7. EJECUCIÓN PRINCIPAL
# ============================================================================
if __name__ == "__main__":
    print("="*70)
    print("🔗 ANÁLISIS DE CORRELACIÓN ENTRE ACTIVOS")
    print("="*70)
    
    # 7.1. Descargar datos para período completo
    precios_completos = descargar_datos_multiactivos(TICKERS, START_DATE, END_DATE)
    
    if len(precios_completos.columns) < 2:
        print("❌ Se necesitan al menos 2 activos para análisis de correlación")
    else:
        # 7.2. Análisis completo
        resultados = analizar_correlaciones(precios_completos)
        
        # 7.3. Mostrar resultados en consola
        print("\n" + "="*70)
        print("📊 RESULTADOS PRINCIPALES")
        print("="*70)
        
        print(f"\n📈 ACTIVOS ANALIZADOS ({len(resultados['precios'].columns)}):")
        print(", ".join(resultados['precios'].columns.tolist()))
        
        print(f"\n🔗 CORRELACIÓN PROMEDIO POR ACTIVO:")
        for ticker, corr in resultados['correlacion_promedio'].items():
            print(f"  {ticker}: {corr:.3f}")
        
        print(f"\n🎯 PARES DESTACADOS:")
        par_max = resultados['par_max_correlacion']
        par_min = resultados['par_min_correlacion']
        print(f"  Mayor correlación: {par_max[0]} vs {par_max[1]} = {resultados['matriz_correlacion'].loc[par_max[0], par_max[1]]:.3f}")
        print(f"  Menor correlación: {par_min[0]} vs {par_min[1]} = {resultados['matriz_correlacion'].loc[par_min[0], par_min[1]]:.3f}")
        
        print(f"\n📅 PERÍODO ANALIZADO:")
        print(f"  Días totales: {len(resultados['retornos'])}")
        print(f"  Desde: {resultados['precios'].index[0].date()}")
        print(f"  Hasta: {resultados['precios'].index[-1].date()}")
        
        # 7.4. Análisis por períodos específicos (opcional)
        print("\n" + "="*70)
        print("🌪️  ANÁLISIS POR PERÍODOS ESPECÍFICOS")
        print("="*70)
        
        if PERIODOS_CRISIS:
            resultados_periodos = analisis_periodos_especificos(TICKERS, PERIODOS_CRISIS)
        
        # 7.5. Generar visualizaciones
        print("\n" + "="*70)
        print("📊 GENERANDO VISUALIZACIONES")
        print("="*70)
        
        crear_visualizaciones(resultados, TICKERS)
        
        print("\n✅ Análisis completado. Gráficos guardados como:")
        print("   - correlacion_heatmap.png")
        print("   - precios_normalizados.png")
        print("   - scatter_correlacion.png")
        
        print("\n" + "="*70)
        print("💡 INTERPRETACIÓN RÁPIDA:")
        print("="*70)
        print("• Correlación cerca de +1: Se mueven JUNTOS (mala diversificación)")
        print("• Correlación cerca de 0: Se mueven INDEPENDIENTE (buena diversificación)")
        print("• Correlación cerca de -1: Se mueven OPUESTOS (cobertura perfecta)")
        print("\n🎯 Para diversificar: busca activos con correlación BAJA o NEGATIVA")