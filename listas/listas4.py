#Elementos mayores que un valor: Escribe una función que tome una lista de números
#y un valor n, y devuelva una nueva lista con los elementos mayores que n.

def mayor_que_n(lista, n):
    lista_mayor = []
    for numero in lista:
        if numero > n: #si el numero es mayor a n lo agrego a la nueva lista
            lista_mayor.append(numero)
    return lista_mayor

valor_n = float(input("Ingrese un valor númerico (Se mostrara todos los elementos de la lista mayores al número ingresado): "))
numeros = [5, 10, 20, 30, 50]
resultado = mayor_que_n(numeros, valor_n)     
print(resultado)