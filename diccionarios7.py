#Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y devuelva la suma de todos los valores.

def suma_valores(dicc):
    suma = 0
    for clave in dicc:
        suma += dicc[clave]
    return suma

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

resultado = suma_valores(diccionario)
print(f"La suma de todos los valores del diccionario es: {resultado}")