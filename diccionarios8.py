#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.

def frecuencia_palabra(lista):
    nuevo_dicc = {}
    for palabra in lista:
        if palabra in nuevo_dicc:
            nuevo_dicc[palabra] += 1
        if palabra not in nuevo_dicc:
            nuevo_dicc[palabra] = 1
    return nuevo_dicc


lista_palabras = ["milanesa", "fideos", "fideos"]
frecuencia = frecuencia_palabra(lista_palabras)
print(f"{frecuencia}")