#Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.

def producto_lista(lista):
    resultado = 1 #arranca en 1 asi al multiplicar el primer número su valor no cambia, quedando igual. (5x1 = 5) y después se multiplica con los demas numeros
    for numero in lista:
        resultado *= numero
    return resultado

numeros = [5, 10, 2]
resultado = producto_lista(numeros)
print(f"La lista es {numeros}")
print(f"La multiplicación de todos los elementos de esta lista da: {resultado}")