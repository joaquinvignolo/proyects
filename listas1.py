#Suma de elementos: Escribe una función que tome una lista de números y devuelva la
#suma de todos los elementos en la lista.

def suma_lista(lista):
    return sum(lista)

numeros = [15, 12, 13, 45, 10]
resultado = suma_lista(numeros)
print(f"La suma de la lista es: {resultado}")