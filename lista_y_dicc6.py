#Inventario de productos: Escribe una función que recibe un diccionario donde las claves son los nombres de los productos y los valores son listas de 
#precios históricos de esos productos. La función debe devolver un nuevo diccionario donde las claves son los nombres de los productos y los valores 
#son el precio promedio de cada producto.

def promedio_producto(dicc):
    nuevo_dicc = {}
    for clave in dicc:
        if clave not in nuevo_dicc:
            nuevo_dicc[clave] = dicc[clave]
    for clave in nuevo_dicc:
        suma = sum(nuevo_dicc[clave])
        promedio = suma / len(nuevo_dicc[clave])
        nuevo_dicc[clave] = [promedio]
    return nuevo_dicc

diccionario = {
    "Montura": [800, 1000, 1250.50],
    "Huevo": [10, 30, 66]
}

resultado = promedio_producto(diccionario)
print(f"El nuevo diccionario es {resultado}")