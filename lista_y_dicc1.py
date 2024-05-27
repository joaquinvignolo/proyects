#Contar palabras en frases: Escribe una función que reciba una lista de frases y
#devuelva un diccionario donde las claves son las palabras y los valores son las
#frecuencias de esas palabras en todas las frases.

def contar_frases(frases):
    palabras = ' '.join(frases).split()  #creo una cadena con las frases y las divido en palabras
    conteo = {} #diccionario
    for palabra in palabras: #itero sobre cada palabra de las palabras
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

frases = ["Mundo hola", "Como va", "Como va"]
resultado = contar_frases(frases)
print(resultado)