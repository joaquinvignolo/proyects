#Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
#valor máximo y el mínimo de la lista.

def max_y_min(lista):
    return max(lista), min(lista)

numeros = [5, 10, 25, 40]
max, min = max_y_min(numeros)
print("El valor máximo de la lista es", max)
print("El valor mínimo de la lista es", min)