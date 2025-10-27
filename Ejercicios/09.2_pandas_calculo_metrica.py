import pandas as pd 

data = {
    'Open': [100.0, 101.5, 99.8, 103.0, 102.5],
    'Close': [101.2, 99.5, 102.8, 102.1, 104.0],
    'Volume': [50000, 45000, 60000, 75000, 80000]
}

df_precios = pd.DataFrame(data)

# Calcula la variación diaria (Cierre - Apertura)
df_precios["Variacion"] = df_precios["Close"] - df_precios["Open"]

print("--- DATAFRAME COMPLETO CON VARIACIÓN ---")
print(df_precios.head())



