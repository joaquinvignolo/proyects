import funciones

def Menu_Principal():
    while True:
        print("\n *** Menú Principal *** ")
        print("1. Medidas de Posición")
        print("2. Medidas de Dispersión")
        print("3. Frecuencias")
        print("4. Intervalos de Clase")
        print("5. Salir")
        try:
            opcion = int(input("Elija una opción (1-5): "))
            if opcion == 1:
                lista = []
                lista = funciones.AGREGAR_ELEMENTOS_INPUT(lista)
                funciones.MEDIDAS_POSICION(lista)
            elif opcion == 2:
                lista = []
                lista = funciones.AGREGAR_ELEMENTOS_INPUT(lista)
                funciones.MEDIDAS_DISPERCION(lista)
            elif opcion == 3:
                lista = []
                lista = funciones.AGREGAR_ELEMENTOS_INPUT(lista)
                funciones.CALCULAR_FRECUENCIAS(lista)
            elif opcion == 4:
                lista = []
                lista = funciones.AGREGAR_ELEMENTOS_INPUT(lista)
                funciones.INTERVALOS_CLASE(lista)
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
