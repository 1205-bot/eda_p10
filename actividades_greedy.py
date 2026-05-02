actividades = [
    {"A", 1, 4},
    {"B", 3, 5},
    {"C", 0, 6},
    {"D", 5, 7},
    {"E", 3, 9},
    {"F", 5, 9},
]

actividades.sort(key=lambda x: x[2])  # Ordenar por tiempo de finalización

seleccionadas = []
ultimo_tiempo_finalizacion = 0

for actividad in actividades:
    nombre, inicio, fin = actividad
    if inicio >= ultimo_tiempo_finalizacion:
        seleccionadas.append(nombre)
        ultimo_tiempo_finalizacion = fin
print("Actividades seleccionadas:", seleccionadas)
