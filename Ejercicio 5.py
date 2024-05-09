def calcular_temp():
    
    print("1. Convertir de grados Celcius a Fahrenheit")
    print("2. Convertir de grados Fahrenheit a Celcius")

    opcion = int(input("Elija su opción: "))

    if opcion == 1:
        temp = float(input("Ingrese la temperatura en celsius: "))
        temp_final = (temp * 9 / 5) + 32
        print (f"La temperatura convertida en grados Fahrenheit sería: {round(temp_final, 2)}")
    elif opcion == 2:
        temp = float(input("Ingrese la temperatura en Fahrenheit: "))
        temp_final = (temp - 32) * 5/9
        print (f"La temperatura convertida en grados Celcius sería: {round(temp_final, 2)}")
    else:
        print("Por favor ingrese '1' o '2'.")

calcular_temp()