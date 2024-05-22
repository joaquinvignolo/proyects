#Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
#sin elementos duplicados.

def sin_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento) #creo una nueva lista en donde no se repitan los elementos que ya aparecen
    return lista_sin_duplicados

elementos = [5, 10, 10, "milanesa", "milanesa"]
resultado = sin_duplicados(elementos)
print("La lista original es", elementos)
print("La nueva lista sin duplicados es", resultado)