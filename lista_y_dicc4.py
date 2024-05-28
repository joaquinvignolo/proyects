#Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y los valores son listas de sus 
#calificaciones. La función debe devolver un nuevo diccionario con las mismas claves pero donde los valores son la calificación promedio de cada 
#estudiante.

def promedio_dicc(dicc):
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
    "joaquin": [8, 8, 8],
    "genaro": [7, 10, 5],
    "ezequiel": [1, 10, 10]
}

resultado = promedio_dicc(diccionario)
print(f"El nuevo diccionario promediado es: {resultado}")