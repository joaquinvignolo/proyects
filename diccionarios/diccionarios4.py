#Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
#y devuelva un nuevo diccionario solo con las claves especificadas.

def claves_especificas(dicc, lista_claves):
    nuevo_diccionario = {}
    for clave in lista_claves:
        if clave in dicc:
            nuevo_diccionario[clave] = dicc[clave]
    return nuevo_diccionario

dicc_original = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

claves_filtrar = ["a", "c"]
resultado = claves_especificas(dicc_original, claves_filtrar)
print(f"{dicc_original}")
print(f"{resultado}")