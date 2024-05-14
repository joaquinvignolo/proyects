#Crear una función recursiva que permita calcular el factorial de un número. Realiza un
#programa principal donde se lea un número validado como entero, el cual es ingresado por
#el usuario y se muestre el resultado del factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    numero = int(input("Ingrese su número y te dare el factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
    
if __name__ == "__main__":
    main()

#Llamada inicial: Se llama a la función factorial(n) desde el programa principal.
#Ejemplo: Al usar 5 que no es igual a 0, el caso base no se cumple y pasamos al siguiente paso.
#Caso recursivo: Se llama a factorial(4) dentro de factorial(5).
#Nuevo llamado: Ahora, n es 4. Se repite el proceso.
#Caso recursivo nuevamente: factorial(4) llama a factorial(3).
#Continúa hasta alcanzar el caso base: Este proceso continúa hasta que factorial(1) llama a factorial(0).
#Caso base: En factorial(0), la función devuelve 1.
#Desenrollamiento de la recursión: A partir de aquí, los valores se van devolviendo hacia arriba. factorial(1) devuelve 1, luego factorial(2) devuelve 2 * 1 = 2, luego factorial(3) devuelve 3 * 2 = 6, y así sucesivamente hasta factorial(5) que devuelve 5 * 24 = 120.
#Resultado final: El resultado final es 120, que es el factorial de 5.