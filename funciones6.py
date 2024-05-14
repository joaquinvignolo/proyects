#Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
#los números pares en la lista.

def devolver_pares(lista):
    numeros_pares = list(filter(lambda x: x % 2 == 0, lista)) #filtra los numeros pares de la lista
    suma_par = sum(numeros_pares) #suma los numeros pares filtrados con anterioridad
    return suma_par 

def main():
    
    numeros = [] #se crea la lista
    cantidad = 0
    
    while cantidad < 7: #permite el ingreso de 7 números
        
        cantidad += 1
        numero = float(input(f"Ingrese el número {cantidad}: "))
        numeros.append(numero)  #agrega cada número a la lista
    
    sumadepares = devolver_pares(numeros) #llamo a la funcion, esta guardara en la variable la suma de los pares de la lista "numeros" que ingreso el usuario
    print(f"La suma de los pares es {sumadepares}") #muestro el la suma de los pares
    
if __name__ == "__main__":
    main()