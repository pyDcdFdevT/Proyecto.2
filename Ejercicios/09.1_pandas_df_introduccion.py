import pandas as pd

precios_cierre = [10.5, 10.8, 11.2, 10.9, 11.5]

df_precios = pd.DataFrame(precios_cierre, columns=["Cierre"])

print("Lista Original:", precios_cierre)
print("\nDataFrame (df_precios):")
print(df_precios.head())
