#Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
#un diccionario donde las claves son las longitudes de las palabras y los valores son
#listas de palabras con esa longitud.

def agrupar_longitud(lista):
    nuevo_diccionario = {}
    for palabra in lista:
        longitud = len(palabra)
        if longitud not in nuevo_diccionario:
            nuevo_diccionario[longitud] = []
        nuevo_diccionario[longitud].append(palabra)
    return nuevo_diccionario

palabras = ["mantel", "pincel", "agua", "rata"]
resultado = agrupar_longitud(palabras)
print(resultado)