#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.

import re

def validar_contrasena(contrasena):
    if len(contrasena) < 8: #Si tiene menos de 8 caracteres devuelve false
        return False
    
    if not re.search(r"[A-Z]", contrasena): #Busca que tenga una mayuscula
        return False
    
    if not re.search(r"[a-z]", contrasena): #Busca que tenga una minuscula
        return False
    
    if not re.search(r"\d", contrasena): #Busca caracteres numericos
        return False
    
    if not re.search(r"[!@#$%^&*()_+{}|:<>?~\-]", contrasena): #Busca simbolos especiales
        return False

    return True #En caso de que pase todas las condiciones solo ahi devuelve true

print("La contraseña debe tener al menos 8 caracteres de longitud y contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial \n")
contrasena = input("Contraseña: ")

if validar_contrasena(contrasena): #Si la contraseña ingresada devuelve true se toma como valida.
    print("Contraseña válida.")
else:
    print("La contraseña no es válida.")
