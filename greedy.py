def cambio(cantidad, denominaciones):
    resultado = []
    while cantidad > 0:
        if(cantidad >= denominaciones[0]):
            
            num = cantidad // denominaciones[0]
            cantidad = cantidad - num * denominaciones[0]
            resultado.append((denominaciones[0], num))
        denominaciones = denominaciones[1:]
    return resultado

print(cambio(1000, [500, 200, 100, 50, 20, 10, 5, 2, 1]))
print(cambio(500, [500, 200, 100, 50, 20, 10, 5, 2, 1]))
print(cambio(300, [500, 200, 100, 50, 20, 10, 5, 2, 1]))
print(cambio(200, [500, 200, 100, 50, 20, 10, 5, 2, 1]))
print(cambio(100, [500, 200, 100, 50, 20, 10, 5, 2, 1]))