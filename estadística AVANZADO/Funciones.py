import math
from math import comb, pow, exp, factorial, sqrt, pi
import scipy.integrate as integrate
from scipy import stats
from scipy.stats import hypergeom

# MEDIDAS DE POSICIÓN

def MEDIA(lista):
    return sum(lista) / len(lista)
    
def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    
    for Numero in lista:
        Cont = 0
        for Elem in lista:
            if Elem == Numero:
                Cont += 1
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)

    if len(Modas) == len(set(lista)):  # set elimina duplicados
        return "No hay moda"
    else:
        return Modas
    
def CALCULAR_MEDIANA(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    
    if longitudLista % 2 == 0:
        medioIzq = listaOrdenada[longitudLista // 2 - 1]
        medioDer = listaOrdenada[longitudLista // 2]
        return (medioIzq + medioDer) / 2
    else:
        return listaOrdenada[longitudLista // 2]

def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def CALCULAR_CUARTILES(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    mediana = CALCULAR_MEDIANA(listaOrdenada)
    if longitudLista % 2 == 0:
        mitad_inferior = listaOrdenada[:longitudLista // 2]
        mitad_superior = listaOrdenada[longitudLista // 2:]
    else:
        mitad_inferior = listaOrdenada[:longitudLista // 2]
        mitad_superior = listaOrdenada[longitudLista // 2 + 1:]

    q1 = CALCULAR_MEDIANA(mitad_inferior)
    q2 = mediana
    q3 = CALCULAR_MEDIANA(mitad_superior)
    
    return q1, q2, q3

def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    suma_resta_cuadrado = sum((x - promedio) ** 2 for x in lista)
    desviacion = (suma_resta_cuadrado / (n - 1)) ** 0.5
    return round(desviacion, 4)

def RANGO(lista):
    return lista[-1] - lista[0]

# FRECUENCIAS

def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    frecuencias_absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    frecuencia_absoluta_acumulada = {}
    acumulador = 0
    for elemento, frecuencia in frecuencias_absolutas.items():
        acumulador += frecuencia
        frecuencia_absoluta_acumulada[elemento] = acumulador
    return frecuencia_absoluta_acumulada

def SOLO_UN_ELEMENTO(lista):
    return list(set(lista))

def CALCULAR_FRECUENCIA_RELATIVA(lista):
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    lista_simple = SOLO_UN_ELEMENTO(lista)
    for elemento in lista_simple:
        absoluta = frecuencia_absoluta[elemento]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(round(frecuencia, 4))
    return frecuencia_relativa

def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    frecuencia_relativa_acumulada = []
    total = 0
    for i in range(len(frecuencia_relativa)):
        total += frecuencia_relativa[i]
        frecuencia_relativa_acumulada.append(round(total, 4))
    return frecuencia_relativa_acumulada

def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    return [elemento * 100 for elemento in frecuencia_relativa]

def CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista):
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    frecuencia_porcentual_acumulada = []
    acumulada = 0
    for elemento in frecuencia_porcentual:
        acumulada += elemento
        frecuencia_porcentual_acumulada.append(round(acumulada, 2))
    return frecuencia_porcentual_acumulada

# INTERVALOS

def CALCULAR_AMPLITUD_INTERVALOS(datos):
    minimo = min(datos)
    maximo = max(datos)
    numero_intervalos = sqrt(len(datos))
    amplitud = (maximo - minimo) / numero_intervalos
    return round(amplitud, 4)

def CALCULAR_INTERVALOS_CLASE(datos):
    cantidad_datos = len(datos)
    numero_intervalos = sqrt(cantidad_datos)
    amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos)
    
    limite_inferior = min(datos)
    limite_superior = limite_inferior + amplitud
    intervalos = []

    while limite_superior <= max(datos):
        intervalos.append((round(limite_inferior, 4), round(limite_superior, 4)))
        limite_inferior = limite_superior
        limite_superior += amplitud
    return intervalos

# COEFICIENTE DE CURTOSIS

def CALCULAR_CURTOSIS(lista):
    n = len(lista)
    if n < 4:
        return "Número insuficiente de datos para calcular la curtosis"
    
    media = MEDIA(lista)
    desviacion = DESVIACION_ESTANDAR(lista)
    suma_cuarta = sum((x - media) ** 4 for x in lista)
    
    kurtosis = (suma_cuarta / (n * (desviacion ** 4))) - 3
    return round(kurtosis, 4)

# FUNCIONES DEL INPUT

def AGREGAR_ELEMENTOS_INPUT(lista):
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y presione enter para confirmar y continuar agregando más datos. \nCuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        valor = input(f"Ingrese dato número {numero_muestra + 1}: ")
        if valor.isdigit():
            lista.append(float(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de la muestra")
                break
            else:
                print("Comando no válido, intente de nuevo.")
        else:
            try:
                valor = float(valor)
                lista.append(valor)
                numero_muestra += 1
            except:
                print("Comando no válido, intente de nuevo.")

    lista = sorted(lista)
    return lista

def MEDIDAS_POSICION(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MÍNIMO.\n 6 = CUARTILES.\n 7 = CURTOSIS.\n ==> "))
        if comando == 1:
            valor = "La > Media Aritmética < de la lista es "
            resultado = MEDIA(lista)
            break
        elif comando == 2:
            valor = "La > Moda < de la lista es "
            resultado = CALCULAR_MODA(lista)
            break
        elif comando == 3:
            valor = "La > Mediana < de la lista es "
            resultado = CALCULAR_MEDIANA(lista)
            break
        elif comando == 4:
            valor = "El > Máximo < de la lista es "
            resultado = lista[-1]
            break
        elif comando == 5:
            valor = "El > Mínimo < de la lista es "
            resultado = lista[0]
            break
        elif comando == 6:
            valor = "Los > Cuartiles < de la lista son "
            resultado = CALCULAR_CUARTILES(lista)
            break
        elif comando == 7:
            valor = "El > Coeficiente de Curtosis < de la lista es "
            resultado = CALCULAR_CURTOSIS(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)

def MEDIDAS_DISPERCION(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = DESVIACIÓN ESTÁNDAR.\n 2 = RANGO.\n ==> "))
        if comando == 1:
            valor = "La > Desviación Estándar < de la lista es "
            resultado = DESVIACION_ESTANDAR(lista)
            break
        elif comando == 2:
            valor = "El > Rango < de la lista es "
            resultado = RANGO(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)
    
def CALCULAR_FRECUENCIAS(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = FRECUENCIA ABSOLUTA.\n 2 = FRECUENCIA ABSOLUTA ACUMULADA.\n 3 = FRECUENCIA RELATIVA.\n 4 = FRECUENCIA RELATIVA ACUMULADA.\n 5 = FRECUENCIA PORCENTUAL.\n 6 = FRECUENCIA PORCENTUAL ACUMULADA.\n ==> "))
        if comando == 1:
            valor = "Las > Frecuencias Absolutas < de la lista son "
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
            break
        elif comando == 2:
            valor = "Las > Frecuencias Absolutas Acumuladas < de la lista son "
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista)
            break
        elif comando == 3:
            valor = "Las > Frecuencias Relativas < de la lista son "
            resultado = CALCULAR_FRECUENCIA_RELATIVA(lista)
            break
        elif comando == 4:
            valor = "Las > Frecuencias Relativas Acumuladas < de la lista son "
            resultado = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista)
            break
        elif comando == 5:
            valor = "Las > Frecuencias Porcentuales < de la lista son "
            resultado = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
            break
        elif comando == 6:
            valor = "Las > Frecuencias Porcentuales Acumuladas < de la lista son "
            resultado = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)

def INTERVALOS_CLASE(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = INTERVALOS CLASE.\n ==> "))
        if comando == 1:
            valor = "Los > Intervalos de Clase < de la lista son "
            resultado = CALCULAR_INTERVALOS_CLASE(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)
