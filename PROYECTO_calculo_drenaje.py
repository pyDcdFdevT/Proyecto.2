# 1. Variables de entrada (en las unidades originales)
volumen_m3 = 500000 
bomba_lmin = 1000

# 2. Variables de conversión (Fundamentos a memorizar: 1 m³ = 1000 L)
litros_por_min = 1000 
segundos_en_minuto = 60
minutos_en_hora = 60
horas_en_dia = 24

litros_total = volumen_m3 * 1000
print(f"El total de litros es de: {litros_total}")

minutos_total = litros_total / bomba_lmin
print(f"El total de minutos es de: {minutos_total}")

horas_total = minutos_total // minutos_en_hora
minutos_sobrantes = minutos_total % minutos_en_hora
print(f"El total de horas es: {horas_total}")
print(f"Los minutos sobrantes: {minutos_sobrantes}")

dias_total = horas_total // horas_en_dia
horas_sobrantes = horas_total % horas_en_dia
print(f"El total de días es: {dias_total}")
print(f"Las horas sobrantes: {horas_sobrantes}")

print(f"La bomba tardará un total de: {dias_total} días, {horas_sobrantes} horas, {minutos_sobrantes} minutos en sacar toda el agua.")


