#Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
#lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
#de puntuación.

def palindromo(palabra):

    palabra_limpia = ''.join(caracter for caracter in palabra if caracter.isalnum()).lower() #isalnum filtra todo lo que no sea caracteres alfanumericos, el ''.join concatena estos caracteres en una cadena
    return palabra_limpia == palabra_limpia[::-1] #itera de derecha a izquierda de principio a fin la palabra y la invierte, si son iguales devuelve true

palabra = input("Ingrese una palabra: ")

if palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")