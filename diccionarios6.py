#Intercambiar valores: Crea una función que tome un diccionario y dos claves, e intercambie los valores de esas dos claves en el diccionario.

def cambio_claves(dicc, clave1, clave2):
    if clave1 in dicc and clave2 in dicc: #ambas claves deben estar en el diccionario
        dicc[clave1], dicc[clave2] = dicc[clave2], dicc[clave1] #intercambia los valores
    else:
        print("Ambas claves deben estar en el diccionario")

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

cambio_claves(diccionario, "a", "c")
print("Con el intercambio", diccionario)