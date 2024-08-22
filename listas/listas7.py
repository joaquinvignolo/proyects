#Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
#elementos en orden inverso.

def invertir_lista(lista):
    lista = lista[::-1] #invierte la lista
    return lista

elementos = ["milanesa", "queso", "crema"]
resultado = invertir_lista(elementos)
print(f"La lista original es {elementos}")
print(f"La lista invertida es {resultado}")