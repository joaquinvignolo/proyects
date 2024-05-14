#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
#ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def convertir_espaciado(texto):
    texto_espacios = '' #Variable con una cadena vacía
    for letra in texto: #Ciclo for que itera en cada letra del texto
        texto_espacios = texto_espacios + letra + ' ' #Mete espacios en cada letra del texto y lo guarda en la variable "textos_espacios"
    return texto_espacios #Devuelve el texto espaciado

def main(): #Programa principal
    texto = input("Ingrese un texto: ")
    texto_espacios = convertir_espaciado(texto) #llama a la función pasando el texto
    print(f"Texto con espacios {texto_espacios}") #muestra el texto ya espaciado

if __name__ == "__main__":
    main()