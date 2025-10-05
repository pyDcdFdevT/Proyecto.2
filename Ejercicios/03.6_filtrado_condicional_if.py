proyectos = {
    "Data_Viz": {"estado": "Pendiente", "prioridad": "Alta"},
    "ETL": {"estado": "En Curso", "prioridad": "Alta"},
    "Modelo_ML": {"estado": "Finalizado", "prioridad": "Media"}
}
proyectos_alta = []
for nombre, datos in proyectos.items():
    if datos["prioridad"] == "Alta":
        proyectos_alta.append(nombre)
print(proyectos_alta)