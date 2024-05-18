#Contar letras: Crea una función que tome una cadena como entrada y devuelva un
#diccionario con el recuento de cada letra en la cadena.

def contar_letras(cadena):
    
    contador_letras = {} #se crea el diccionario

    for letra in cadena: #itero sobre cada letra de la cadena

        if letra in contador_letras: #si la letra ya estaba se aumenta su contador
            contador_letras[letra] += 1
        #sino esta la letra se agrega como primera vez
        else:
            contador_letras[letra] = 1
    
    return contador_letras

cadena_user = input("Ingrese una frase: ")
resultado = contar_letras(cadena_user)
print(resultado)