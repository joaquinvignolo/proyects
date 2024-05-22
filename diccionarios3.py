#Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
#nuevo que combine ambos (en caso de conflicto, usa los valores del segundo diccionario).

def ambos_diccionarios(diccionario1, diccionario2):
    diccionario1.update(diccionario2) #el .update combina ambos diccionarios
    return diccionario1               #si hay claves en comun el segundo dicc sobrescribira las mismas.

dic1 = {
    "nombre": "patroclo"
}

dic2= {
    "apellido": "refulgente"
}

combinacion = ambos_diccionarios(dic1, dic2)
print(f"El nuevo super diccionario es: {combinacion}")