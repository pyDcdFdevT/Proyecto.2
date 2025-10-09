salarios = [2000, 2500, 3000, 4000, 4500, 6000]

L = len(salarios)
indice_1 = (L  // 2) - 1
indice_2 = L // 2

valor_1 = salarios[indice_1]
valor_2 = salarios[indice_2]

mediana = (valor_1 + valor_2) / 2

print(f"La mediana de los salarios es: {mediana}")