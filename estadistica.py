import statistics
from tabulate import tabulate

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_moda(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    
    moda_frecuencia_maxima = max(frecuencias.values())
    moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]

    if len(set(frecuencias.values())) == 1:
        return None, None
    else:
        return moda, moda_frecuencia_maxima

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    return statistics.median(lista_ordenada)

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista)
    return desviacion_estandar

def calcular_varianza(lista):
    varianza = statistics.variance(lista)
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
    print('Ingrese los datos uno por uno (ENTER), luego para ir al menú ingrese "n" \n')
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
            print(tabulate([["MEDIA", calcular_media(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 2:
            moda, frecuencia = calcular_moda(numeros)
            if moda is None:
                print("No hay moda en los datos.")
            else:
                print(tabulate([["MODA", f"{moda} (Frecuencia: {frecuencia})"]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 3:
            print(tabulate([["MEDIANA", calcular_mediana(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 4:
            print(tabulate([["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 5:
            print(tabulate([["VARIANZA", calcular_varianza(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        else:
            print("Opción no válida.")
        
        opcion = menu()

if __name__ == "__main__":
    main()
