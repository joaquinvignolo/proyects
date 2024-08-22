#Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
#nuevo que invierta las claves y los valores.

def diccionario_inverso(dicc):
    dicc_inverso = {valor: clave for clave, valor in dicc.items()} #las claves pasan a ser valores y viceversa
    return dicc_inverso

diccionario_original = {
    "nombre": "patroclo"
}
inverso = diccionario_inverso(diccionario_original)
print(f"El diccionario original es: {diccionario_original}")
print(f"El inverso es {inverso}")