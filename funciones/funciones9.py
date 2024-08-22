#Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
#lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.

def ordenar_lista(lista_cadenas):
    lista_cadenas.sort(key=str.lower) #sort ordena y modifica la lista sin hacer una nueva, key=str.lower convierte la cadena a minusculas
    return lista_cadenas

lista = ["payaSo", "Maniqui", "Arbol", "ex"]
ordenar_lista(lista)
print(f"La lista ordenada quedaría así: {lista}")