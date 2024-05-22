#Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
#tuplas (clave, valor) y actualice el diccionario con esas tuplas.

def actualizar_diccionario(dicc, lista_tuplas):
    for clave, valor in lista_tuplas:
        dicc[clave] = valor

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(f"{diccionario}")
tuplas = [("a", 10), ("b", 20), ("c", 30)]
actualizar_diccionario(diccionario, tuplas)
print(f"{diccionario}")