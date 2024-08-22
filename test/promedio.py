def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [5, 8, 10, 3, 9]
print ("El promedio de la lista es:", calcular_promedio(numeros))