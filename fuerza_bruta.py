#Complegidad n cuadrada o logaritmica dependiendo del caso
#Tarda tiempo pero siempre encuantra una solucion, aunque muy deficiente

from string import ascii_letters, digits
from itertools import product

caracteres = ascii_letters + digits

def buscador(contraseña):
    archivo = open("contraseñas.txt", "w")
    
    if 3<= len(contraseña) <= 10:
        for longitud in range(3, 11):  # Limitar la longitud de la contraseña
            for intento in product(caracteres, repeat=longitud):
                intento_contraseña = ''.join(intento)
                
                archivo.write(intento_contraseña + "\n")  # Escribir cada intento en el archivo
                if intento_contraseña == contraseña:
                    archivo.write(intento_contraseña + "\n")
                    archivo.close() 
    return None