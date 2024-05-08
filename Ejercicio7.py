#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. 
# El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. 
# El juego debe continuar hasta que el jugador adivine correctamente el número.

import random

def adivina_adivinador():
    numero = random.randint(1,100) #Genera un random entre el 1 y el 100
    
    print("Hola, ¡Vamos a jugar un juego! Consiste en lo siguiente:")
    print("Tengo un número entre el 1 y el 100 en la mente")
    print("Te toca adivinar cuál es. Te ire dando pistas. Tienes intentos infinitos no te preocupes.\n")

    while True: #Se repite el ciclo hasta que se cumpla la condición
        numero_usuario = int(input("Ingrese el número: "))
        
        if numero_usuario < numero:
            print("Mas alto")
        if numero_usuario > numero:
            print("Mas bajo")
        if numero_usuario == numero:
            print(f"¡Felicidades, has acertado! El número era {numero}")
            break #Rompe la cadena
     
adivina_adivinador() #Llama a la función para que arranque el juego
