def calcular_estadisticas(lista):
    lista_ordenada = sorted(lista)
    L = len(lista_ordenada)
    
    #---- 2. CÁLCULO DE LA MEDIA (El MAESTRO) ---
    media = sum(lista_ordenada)/ L
    
    #--- 3. CÁLCULO DE LA MEDIANA (El LOBO, los PALILLOS chinos y el guante de BOXEO)
    if L % 2 != 0:
        # Longitud IMPAR (Solo un valor central)
        indice_central = L // 2
        mediana = lista_ordenada[indice_central]
    else:
        # Longitud PAR (Promedio de dos valores centrales)
        indice_1 = (L // 2) - 1
        indice_2 = L // 2
        
        # OBTENEMOS LOS VALORES (Los Dos Billetes)
        valor_1 = lista_ordenada[indice_1] # <--- ¡USANDO lista_ordenada!
        valor_2 = lista_ordenada[indice_2] # <--- ¡USANDO lista_ordenada!
        
        # ABRAZO y GUANTE (Promedio)
        mediana = (valor_1 + valor_2) / 2
    
    #--- 4. CÁLCULO DE LA MODA (La MODELO y repetición)
    frecuencias = {}
    for num in lista_ordenada:
        frecuencias[num] = frecuencias.get(num , 0) + 1
    moda = max(frecuencias, key=frecuencias.get)
    
    return media, mediana, moda

datos = [10, 10, 20, 30, 30, 30, 40, 50]
media, mediana, moda = calcular_estadisticas(datos)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

    

    