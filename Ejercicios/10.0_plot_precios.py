import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos de prueba
precios_test = [20.0, 20.5, 19.9, 21.0, 21.15, 20.8]

# Función dominada del Ejercicio 10/10
def preparar_datos_quant(precios):
    df = pd.DataFrame({'Price': precios})
    # Aseguramos el índice de tiempo (Paso crítico para graficar)
    df.index = pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03', 
                               '2025-01-06', '2025-01-07', '2025-01-08'][:len(precios)])
    df['LogReturn'] = np.log(df['Price'] / df['Price'].shift(1))
    return df.dropna()

df_datos = preparar_datos_quant(precios_test)

# -----------------------------------------------------
# TU CÓDIGO AQUÍ (Visualización)
# -----------------------------------------------------

# 1. Crea la figura y el eje para el gráfico.
plt.figure(figsize=(10, 5)) 

# 2. Genera el gráfico de línea usando la columna 'Price'.
# Pista: plt.plot(df_datos.index, df_datos['Price'], label='Precios de Cierre')

... 

# 3. Añade título, etiquetas y la leyenda (Best Practice)
plt.title('Evolución de Precios de Cierre')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.grid(True)

# 4. Muestra el gráfico
plt.show()