#10.Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def primera_aparacion(lista, n):
    if n in lista:
        return lista.index(n)
    if n not in lista:
        return -1

valor_n = 40
numeros = [10, 20, 30, 20]
aparacion = primera_aparacion(numeros, valor_n)
print(f"El índice de {valor_n} es {aparacion}")