#Ejercicio 8: Generador de Contraseñas Aleatorias
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
# La contraseña debe tener una longitud de al menos 12 caracteres y 
# debe contener una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales. 
# El programa debe mostrar la contraseña generada al usuario.

import random
import string

def generar_contrasena():
    longitud_minima = 12
    longitud = random.randint(longitud_minima, longitud_minima + 3) #Da una longitud de entre 12 a 15 caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation #Crea una cadena llamada caracteres que contiene todas las letras (mayúsculas y minúsculas), dígitos y caracteres especiales disponibles.
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) #Genera la contraseña utilizandos caracteres random en un largo de 12.
    return contrasena

contrasena = generar_contrasena()
print(f"Tu contraseña generada es: {contrasena}")