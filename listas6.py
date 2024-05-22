#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def contar_elementos(lista, elemento):
    cantidad = 0
    for item in lista:
        if item == elemento: #si el item en este caso "fideos" esta en la lista se suma cada vez que aparece y se guarda en la variable cantidad
            cantidad += 1
    return cantidad

valor_elemento = "fideos"
elementos = ["milanesa", "papas", "fideos", "fideos", "fideos"]
repeticiones = contar_elementos(elementos, valor_elemento)
print(f"La cantidad de repeticiones de {valor_elemento} es de {repeticiones}")