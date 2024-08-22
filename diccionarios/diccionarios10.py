#Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de valores únicos en el diccionario.

def valores_unicos(dicc):
    unicos = []
    for clave in dicc:
        valor = dicc[clave]
        es_unico = True
        for otra_clave in dicc:
            if otra_clave != clave and dicc[otra_clave] == valor:
                es_unico = False
                break
        if es_unico:
            unicos.append(valor)
    return unicos

diccionario = {
    "a": 1,
    "b": 2,
    "c": 1
}

nueva_lista = valores_unicos(diccionario)
print(nueva_lista)