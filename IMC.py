peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura**2
print(f"Su indice de masa corporal es {round(imc, 2)}")