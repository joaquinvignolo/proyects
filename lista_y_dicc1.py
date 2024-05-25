#Contar palabras en frases: Escribe una función que reciba una lista de frases y
#devuelva un diccionario donde las claves son las palabras y los valores son las
#frecuencias de esas palabras en todas las frases.

from collections import Counter

def contar_frases(frases):
    palabras = ' '.join(frases).split() #combina las frases en una cadena y las cuenta
    return Counter(palabras)

frases = ["Mundo hola", "Como va", "Como va"]
resultado = contar_frases(frases)
print(resultado)