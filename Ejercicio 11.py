#Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
# Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
# En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. 
# El juego debe terminar cuando el programa adivine el número correcto.

def adivinar_numero():
    
    print("Piensa en un número entre 1 y 100.")
    input("¿Listo? (Toca cualquier tecla): ")
    
    inicio = 1
    fin = 100
    
    while inicio <= fin:
        
        busqueda = (inicio + fin) // 2
        
        respuesta = input(f"¿Es {busqueda} tu número? Escribe si es 'mayor', 'menor' o 'igual': ").lower()
        
        if respuesta == "igual":
            print(f"¡Gane! Tu número es {busqueda}.")
            break
        
        elif respuesta == "mayor":
            inicio = busqueda + 1

        elif respuesta == "menor":
            fin = busqueda - 1
        
        else:
            print("Por favor, ingresa 'mayor', 'menor' o 'igual'.")

adivinar_numero()