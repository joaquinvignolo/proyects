#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
#valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
#máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    return max(lista), min(lista)

def main():
    
    cantidad = 0
    numeros = []
    while cantidad < 5: #permite el ingreso de 5 números
        
        cantidad += 1
        numero = float(input(f"Ingrese el número {cantidad}: "))
        numeros.append(numero)  #agrega cada número a la lista
        max, min = calcularMaxMin(numeros) #llama a la función y devuelve el maximo y minimo valor de la lista ingresada por el usuario
    
    print(f"Número de mayor valor: {max}")
    print(f"Número de mínimo valor: {min}")

if __name__ == "__main__":
    main()