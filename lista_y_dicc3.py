#Diccionario de listas: Escribe una función que tome un diccionario donde los valores
#son listas y devuelva una lista que contenga todos los elementos de las listas del diccionario.

def diccionario_listas(dicc):
    lista_epica = []
    for lista in dicc.values():
        lista_epica.extend(lista)
    return lista_epica

diccionario = {
    "a": ["carne", "pollo"],
    "b": ["salsa", "queso"],
    "c": ["picante"]
    }

lista_final = diccionario_listas(diccionario)
print(f"La lista extendida es {lista_final}")