#Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. 
# Puedes hacerlo con una lista predefinida de palabras.

import random

def palabra_secreta():
    palabras = ["OMG", "LOL", "CHAD", "SIGMA", "MEME", "XD"]
    return random.choice(palabras)

def juego_ahorcado():
    palabra = palabra_secreta()
    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes que adivinar que palabra estoy pensando, tienes 3 intentos")
    print("Las palabras son: OMG, LOL, CHAD, SIGMA, MEME, XD")
    intentos = 3
    while intentos > 0:
        palabra_user = input("Ingresa tu palabra: ").upper()
        if palabra_user == palabra:
            print ("Felicidades has ganado")
            break
        else:
            intentos -= 1
            print(f"Has fallado. Te quedan {intentos} intentos")
    else:
        print("No tienes mas intentos D:")
        print(f"La palabra era {palabra}")

juego_ahorcado()
