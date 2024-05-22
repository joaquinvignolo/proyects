#Mostrar las frecuencias.

import statistics
from collections import Counter

def calcular_media(lista):
    return statistics.mean(lista) #Calcula la suma de todos los elementos dividida por el número total de elementos.

def calcular_moda(lista):
    moda = statistics.mode(lista) #Calcula la moda buscando el valor que de la lista mas se repite
    frecuencia = lista.count(moda) #Cuenta cuantas veces aparece el dato de la moda
    return moda, frecuencia

def calcular_mediana(lista):
    return statistics.median(lista) #Calcula el valor que se encuentra en la posición central de la lista cuando los datos están ordenados en orden ascendente

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista) # n - 1, Calcula la medida de dispersión que indica cuánto se alejan los valores de la media
    return desviacion_estandar

def calcular_varianza(lista):
    varianza = statistics.variance(lista) #Calcula la media de los cuadrados de las desviaciones respecto a la media
    return varianza

def menu():
    
    opcion = None
    
    try:
        
        print("\n")
        print("0. Para cerrar el menú.")
        print("1. Visualizar la MEDIA.")
        print("2. Visualizar la MODA.")
        print("3. Visualizar la MEDIANA.")
        print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
        print("5. Visualizar la VARIANZA.\n")
        
        opcion = int(input("Ingrese el número de la opción que desea visualizar: "))
    
    except ValueError:    
        print("Por favor, ingrese un número válido.")
    return opcion

def ingresar_datos():
    cantidad = 0
    numeros = []
    print('Cuando termine de ingresar los datos escriba "n" para abrir el menú \n')
    while True:
        numero = input(f"Ingrese el dato número {cantidad + 1}: ")
        if numero.lower() == "n":
            break
        else:
            try:
                numero = float(numero)
                cantidad += 1
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'n' para terminar.")
    return numeros

def main():
    numeros = ingresar_datos()
    opcion = menu()
    
    while opcion != 0:
        
        if opcion == 1:
            print(f"La media es: {calcular_media(numeros)}")
        elif opcion == 2:
            moda, frecuencia = calcular_moda(numeros)
            print(f"La moda es: {moda} y se repite {frecuencia} veces.")
        elif opcion == 3:
            print(f"La mediana es: {calcular_mediana(numeros)}")
        elif opcion == 4:
            print(f"La desviación es: {calcular_desviacion(numeros)}")
        elif opcion == 5:
            print(f"La varianza es: {calcular_varianza(numeros)}")
        else:
            print("Opción no válida.")
        
        opcion = menu()

if __name__ == "__main__":
    main()
    