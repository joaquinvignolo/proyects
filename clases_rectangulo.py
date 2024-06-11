#Crea una clase llamada "Rectangulo" que represente un rectángulo
#Que tenga los siguientes atributos:
#Base y Altura
#La clase debe tener los siguientes métodos
#calcular_area()
#calcula_perimetro()
#Crea una instancia de la clase Rectangulo
#Con una base -5 y una altura -3
#Luego mostrar

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2
    
rectangulo = Rectangulo(-5, -3)

print(f"El área del rectángulo es {rectangulo.calcular_area()}")
print(f"El perímetro del rectángulo es {rectangulo.calcular_perimetro()}")