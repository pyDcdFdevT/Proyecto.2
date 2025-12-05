import pandas as pd
import numpy as np

# 8 días de precios de prueba
data = {'Close': [100.0, 100.5, 99.8, 102.0, 101.5, 98.0, 99.5, 99.0]}
df = pd.DataFrame(data)

# -----------------------------------------------------
# TU CÓDIGO AQUÍ (5 pasos en orden)
# -----------------------------------------------------

# 1. Calcule LogReturn (df['LogReturn']) y la Desviación Estándar (std_diaria)
# (Pista: Recuerda manejar el NaN inicial)

# 2. Calcule el Umbral de Volatilidad (umbral = 2 * std_diaria)

# 3. Filtre los días de 'Riesgo Crítico' (Pérdida AND Movimiento Anormalmente Alto)
# Pista: abs(df['LogReturn']) > umbral
# (Guarda el resultado en df_critico)

# 4. Calcule la media de LogReturn solo para df_critico (media_critica)

# 5. Anualice la Volatilidad general (std_anual)
# -----------------------------------------------------

# Imprimir Resultados para la Interpretación
print("--- Análisis de Riesgo Crítico (Repaso) ---")
print(f"Volatilidad Diaria (σ): {std_diaria:.4f} ({std_diaria * 100:.2f}%)")
print(f"Volatilidad Anualizada: {std_anual:.4f} ({std_anual * 100:.2f}%)")
print(f"Media de Pérdidas Críticas: {media_critica:.4f} ({media_critica * 100:.2f}%)")
print("\nDataFrame de Días Críticos:")
print(df_critico)