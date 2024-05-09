#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. 
# El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. 
# El programa debe manejar números enteros grandes y mostrar el resultado.

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i #Esto es lo mismo que factorial = factorial * i.
    return factorial

try: #Utilizo try por si se ingresa un valor que no sea un numero te salte un error
    
    numero = int(input("Ingresa un número entero para calcular su factorial: "))
    
    if numero < 0:
        print("Ingrese un numero positivo.")
    else:
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Debes ingresar un número entero.")
