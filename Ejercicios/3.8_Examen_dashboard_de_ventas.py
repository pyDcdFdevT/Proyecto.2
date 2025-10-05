ventas_regionales = {
    "Norte": [1500.0, 1500.0, 1800.0, 1500.0, 1200.0],  # Ventas en USD
    "Sur": [1100.0, 900.0, 1100.0, 1400.0, 1100.0],
    "Este": [2500.0, 2200.0, 2500.0, 2000.0, 2500.0]
}
todas_las_ventas = [] 
for ventas in ventas_regionales.values():
    todas_las_ventas.extend(ventas)
todas_las_ventas.sort()  #ya tengo todas las ventas en una lista
venta_media_global = sum(todas_las_ventas)/len(todas_las_ventas)
print(venta_media_global) #1)VENTA MEDIA GLOBAL

venta_maxima_global = max(todas_las_ventas)
print(venta_maxima_global) #2)VENTA MÁXIMA GLOBAL

sur = ventas_regionales["Sur"]
conteo_sur = {}
for nota in sur:
    conteo_sur[nota] = conteo_sur.get(nota, 0) + 1
max_frecuencia = max(conteo_sur.values())
moda_sur = [nota for nota, freq in conteo_sur.items() if freq == max_frecuencia]
print(moda_sur) #3)MODA SUR

for region, ventas in ventas_regionales.items():
    promedio = sum(ventas) / len(ventas)
    print(f"Promedio de {region}: {promedio}")

promedios_regionales = {region: sum(ventas) / len(ventas) for region,
ventas in ventas_regionales.items()} #4)PROMEDIOS REGIONALES

dashboard = {
    "venta_media_global": venta_media_global,
    "venta_maxima_global": venta_maxima_global,
    "moda_sur": moda_sur,
    "promedios_regionales": promedios_regionales
}

print(dashboard)