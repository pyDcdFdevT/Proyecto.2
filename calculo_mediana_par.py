ingresos_par = [500, 300, 700, 400, 600, 800]
ingresos_par.sort()
print(ingresos_par)
indice_inferior = len(ingresos_par) // 2-1
indice_superior = len(ingresos_par) // 2

mediana = (ingresos_par[indice_inferior] + ingresos_par[indice_superior]) / 2
print(mediana)