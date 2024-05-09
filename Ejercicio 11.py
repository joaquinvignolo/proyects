#Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
# Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
# En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. 
# El juego debe terminar cuando el programa adivine el número correcto.

def adivinar_numero():
    
    print("Piensa en un número entre 1 y 100.")
    input("Presione la tecla enter cuando quiera empezar: ")
    
    inicio = 1
    fin = 100
    
    while inicio <= fin: #Se ejecuta siempre que la variable incio sea menor o igual a la variable fin
        
        busqueda = (inicio + fin) // 2 #La busqueda va a ser 50, arranca desde ahí
        
        respuesta = input(f"¿Es {busqueda} tu número? Escribe si es 'mayor', 'menor' o 'igual': ").lower()
        
        if respuesta == "igual":
            print(f"¡Gane! Tu número es {busqueda}.")
            break
        
        elif respuesta == "mayor":
            inicio = busqueda + 1     #Descarta todos los numeros debajo del 50

        elif respuesta == "menor": 
            fin = busqueda - 1        #Descarta todos los numeros arriba del 50
        
        else:
            print("Por favor, ingresa 'mayor', 'menor' o 'igual'.") #Se ejecute en caso de que la respuesta del usuario no sea "mayor", "menor" o "igual"

adivinar_numero()