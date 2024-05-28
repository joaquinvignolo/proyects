#Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
#con la frecuencia de cada letra en la cadena.

def contar_letras(cadena):
    contador_de_letras = {} #creo el diccionario
    for letra in cadena:
        if letra in contador_de_letras: 
            contador_de_letras[letra] += 1  #si la letra ya esta en el contador aumenta su valor
        else:
            contador_de_letras[letra] = 1 #si no esta se agrega como primera vez
    return contador_de_letras

cadena_user = input("Ingrese una cadena: ")
contador = contar_letras(cadena_user)
print(f"{contador}")