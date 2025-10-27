# Lección 1: Retornos simples vs logarítmicos (ejemplo práctico)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (precios de cierre)
data = {'Close': [100.0, 101.5, 99.8, 103.0, 102.1]}
df = pd.DataFrame(data)

# 1) Retorno simple (pct_change)
# .pct_change() calcula (P_t - P_{t-1}) / P_{t-1}
df['Return_simple'] = df['Close'].pct_change()

# 2) Retorno logarítmico
# np.log(P_t / P_{t-1}) OR np.log1p(df['Return_simple']) que es más estable numéricamente
df['Return_log'] = np.log(df['Close'] / df['Close'].shift(1))
# Alternativa equivalente y numéricamente estable:
# df['Return_log_alt'] = np.log1p(df['Return_simple'])

# 3) Observaciones importantes:
# - La primera fila será NaN (no existe P_{t-1})
# - Podemos rellenar NaN si queremos (por ejemplo con 0), pero en análisis estadístico normalmente se ignora la primera observación.
df_filled = df.copy()
df_filled['Return_simple'] = df_filled['Return_simple'].fillna(0)
df_filled['Return_log'] = df_filled['Return_log'].fillna(0)


# 4) Retorno acumulado
# Acumulado multiplicativo usando retornos simples:
df['CumReturn_simple'] = (1 + df['Return_simple']).cumprod() - 1
# Acumulado en log-space (suma de log-returns), luego convertimos a simple:
df['CumReturn_log'] = np.exp(df['Return_log'].cumsum()) - 1

# 5) Comparar aproximación simple vs log (ver cuán parecidos son)
df['Diff_log_vs_simple'] = df['Return_log'] - np.log1p(df['Return_simple'])  # debería ser ~0
# (opcional) verificar la diferencia absoluta
df['AbsDiff'] = df['Diff_log_vs_simple'].abs()

# Mostrar resultados
print(df)

# 6) Visualización sencilla
plt.figure(figsize=(10,4))
plt.plot(df['CumReturn_simple'], marker='o', label='CumReturn simple')
plt.plot(df['CumReturn_log'], marker='x', label='CumReturn log (convertido)')
plt.title('Retornos acumulados: simple vs log (mismo resultado pract.)')
plt.legend()
plt.grid(True)
plt.show()
