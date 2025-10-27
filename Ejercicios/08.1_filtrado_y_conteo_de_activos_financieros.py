#Misión N° 5: Filtrado y Conteo de Activos Financieros
#Como estamos enfocando tus estudios en Finanzas, vamos a 
# usar un escenario de análisis de activos. Queremos saber 
# cuántos de nuestros activos son de Alto Riesgo (riesgo > 7).

#Aquí tienes la lista de tu cartera de inversión simulada:

cartera_inversion = [
    {"simbolo": "BBVA", "riesgo": 5, "pais": "España", "clase": "bancaria"},
    {"simbolo": "TSLA", "riesgo": 9, "pais": "EE. UU.", "clase": "tecnologica"},
    {"simbolo": "IBEX", "riesgo": 3, "pais": "España", "clase": "fondo"},
    {"simbolo": "NVDA", "riesgo": 8, "pais": "EE. UU.", "clase": "tecnologica"},
    {"simbolo": "DAX", "riesgo": 4, "pais": "Alemania", "clase": "fondo"}
]

# Necesitas una variable para contar los activos de alto riesgo:
# ============================================================
# 💼 MISIÓN N°5: FILTRADO Y CONTEO DE ACTIVOS FINANCIEROS
# ============================================================

cartera_inversion = [
    {"simbolo": "BBVA", "riesgo": 5, "pais": "España", "clase": "bancaria"},
    {"simbolo": "TSLA", "riesgo": 9, "pais": "EE. UU.", "clase": "tecnologica"},
    {"simbolo": "IBEX", "riesgo": 3, "pais": "España", "clase": "fondo"},
    {"simbolo": "NVDA", "riesgo": 8, "pais": "EE. UU.", "clase": "tecnologica"},
    {"simbolo": "DAX", "riesgo": 4, "pais": "Alemania", "clase": "fondo"}
]

contador_alto_riesgo = 0

for activo in cartera_inversion:
    riesgo = activo["riesgo"]
    if riesgo > 7:
        contador_alto_riesgo += 1
        print(f"¡Activo de ALTO RIESGO encontrado: {activo["simbolo"]}!")
        
print(f"Hay {contador_alto_riesgo} activos de alto riesgo en la cartera.")


    