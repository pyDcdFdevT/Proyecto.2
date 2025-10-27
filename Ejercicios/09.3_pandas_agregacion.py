import pandas as pd

# Datos de mercado simulados
data = {
    'Open': [100.0, 101.5, 99.8, 103.0, 102.5],
    'Close': [101.2, 99.5, 102.8, 102.1, 104.0]
}

df_precios = pd.DataFrame(data)
df_precios['Variacion'] = df_precios['Close'] - df_precios['Open']

# --- TU CÓDIGO AQUÍ ---

# 1. Calcula el precio promedio de cierre
promedio_cierre = df_precios["Close"].mean() # <-- Accede a la columna 'Close' y usa el método .mean()

# 2. Calcula la volatilidad (desviación estándar) de las variaciones
volatilidad = df_precios["Variacion"].std() # <-- Accede a la columna 'Variacion' y usa el método .std()

# 3. Imprime los resultados
print(f"Precio Promedio de Cierre: {promedio_cierre:.2f}")
print(f"Volatilidad Diaria (Desv. Std.): {volatilidad:.2f}")

def analizar_variacion(df):
    promedio = df["Close"].mean()
    volatilidad = df["Variacion"].std()
    return {
        "Promedio_Cierre": promedio,
        "Volatilidad_Variacion": volatilidad
    }