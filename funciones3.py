#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
#función en un programa principal que lea el radio de una circunferencia y muestre su área y
#perímetro.

import math #para poder usar "pi"

def calcular_circunferencia(radio):
    area = math.pi * radio ** 2 #calcula el área
    perimetro = 2 * math.pi * radio #calcula el perimetro
    return area, perimetro #devuelve area y perimetro

def main():
    radio = float(input("Ingrese el radio de la circunferencia: ")) #el usuario ingresa el radio
    area, perimetro = calcular_circunferencia(radio) #llama a la función y devuelve el area y perimetro del valor radio que ingreso el usuario
    print(f"El área es: {area}")
    print(f"El perímetro es: {perimetro}")
    
if __name__ == "__main__":
    main()
    