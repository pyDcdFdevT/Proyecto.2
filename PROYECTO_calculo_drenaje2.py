# 1. Variables de entrada (en las unidades originales)
volumen_m3 = 500000
bomba_ls = 1000

# 2. Variables de conversión (Fundamentos a memorizar: 1 m³ = 1000 L)
litros_por_m3 = 1000
segundos_en_minuto = 60
minutos_en_hora = 60
horas_en_dia = 24

volumen_total_litros = volumen_m3 * litros_por_m3
print(f"Volumen total en Litros: {volumen_total_litros}")

tiempo_total_segundos = volumen_total_litros / bomba_ls
print(f"Tiempo total en segundos : {tiempo_total_segundos}")
total_minutos = tiempo_total_segundos // segundos_en_minuto
segundos_restantes = tiempo_total_segundos % segundos_en_minuto
print(f"Total de minutos: {total_minutos}")
print(f"segundos restantes: {segundos_restantes}")
total_horas = total_minutos // minutos_en_hora
minutos_restantes = total_minutos % minutos_en_hora
print(f"Total de horas: {total_horas}")
print(f"Minutos restantes: {minutos_restantes}")
total_dias = total_horas // horas_en_dia
horas_restantes = total_horas % horas_en_dia
print(f"Total en días: {total_dias}")
print(f"Horas restantes: {horas_restantes}")

print("\n--- Resultado del Drenaje ---")
print(f"Volumen total de la laguna: {volumen_total_litros} Litros")
print(f"El tiempo de drenaje es:")
print(f"    {total_dias} días,")
print(f"    {horas_restantes} horas,")
print(f"    {minutos_restantes} minutos y")
print(f"    {segundos_restantes} segundos.")