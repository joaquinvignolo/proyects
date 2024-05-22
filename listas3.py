#Promedio de una lista: Crea una función que calcule el promedio de los números en
#una lista dada.

def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [5, 10, 20 ,30 , 40]
resultado = calcular_promedio(numeros)
print(f"El promedio de la lista dada es: {resultado}")