#Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
#diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def numeros_cuadrados(n):
    nuevo_diccionario = {}
    for i in range(1, n + 1):
        nuevo_diccionario[i] = i ** 2
    return nuevo_diccionario

valor_n = int(input("Ingrese un valor para n: "))
if valor_n < 1:
    print("Ingrese un numero mayor a 0")
else: 
    resultado = numeros_cuadrados(valor_n)
    print(f"{resultado}")