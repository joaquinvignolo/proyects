#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
#devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
#hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
#3 oportunidades.

def verificar_login(nombre, password):
   
    nombre_verdadero = 'usuario1'
    contraseña_verdadera = 'asdasd'
    
    if nombre == nombre_verdadero and password == contraseña_verdadera: #verifica si el nombre y contraseña que ingrese el usuario en el programa principal sean los dados con anterioridad
        return True
    else:
        return False

def intentosmax(intentos):
    
    if intentos >= 3:
        print("No te quedan intentos")
        return True
    else:
        return False

def main():
    
    intentos = 0
   
    while intentos < 3:
       
        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña de usuario: ")
        
        if verificar_login(nombre, password):
            print("Ingreso con éxito")
            break #rompe el ciclo al ingresar con exito
        else:
            print("Nombre o contraseña incorrecta, intente otra vez.")
            intentos += 1 #se suman intentos por cada error de logeo
    
    if intentosmax(intentos):
        print("Ha superado el límite de intentos") #al momento de pasar los 3 intentos se llama a esta función y salta este msj

if __name__ == "__main__":
    main()