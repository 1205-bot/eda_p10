from time import time
from fuerza_bruta import buscador

t0 = time()
contraseña = input("Ingrese la contraseña a buscar: ")
buscador(contraseña)
t1 = time()
print(f"Tiempo de ejecución: {t1 - t0} segundos")
