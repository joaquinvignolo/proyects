#Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
#que sea la concatenación de ambas.

def unir_listas(lista1, lista2):
    nueva_lista = lista1 + lista2 #concateno ambas listas para crear una nueva
    return nueva_lista

elementos1 = ["milanesa", "fideos"]
elementos2 = ["chocotorta", "durazno"]
union_listas = unir_listas(elementos1, elementos2)
print(f"La nueva super lista es: {union_listas}")