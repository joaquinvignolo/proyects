try: #Utilizo try para que salte un error en caso de que el usuario decida ingresar un dato que no sea númerico
   temp = float(input("Ingrese la temperatura en celsius: "))
   temp_final = (temp * 9 / 5) + 32
   print (f"La temperatura convertida en grados Fahrenheit sería: {round(temp_final, 2)}")

except ValueError:
    print("Por favor ingrese datos númericos.")