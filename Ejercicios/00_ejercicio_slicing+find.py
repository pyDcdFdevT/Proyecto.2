data = "COD381_Diego_DS_Toledo_PYTHON_2025"

# Encontrar los puntos de corte (los guiones bajos)
p1 = data.find("_")
p2 = data.find("_", p1 + 1)
p_ds = data.find("_DS_")
p_year = data.find("PYTHON_")

# Slicing basado en las posiciones encontradas
codigo_numerico = data[3:p1]
nombre = data[p1 + 1 : p2].lower() # Extrae el nombre y lo convierte a minúsculas
YYYY = data[p_year + len("PYTHON_"):] # Empieza después de 'PYTHON_' y va hasta el final

print(f"El usuario {nombre} con código {codigo_numerico} se graduará en {YYYY}.")

