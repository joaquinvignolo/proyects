import tkinter as tk

#aplico el try para evitar el ingreso de algo que no sea un número float, en caso de hacerlo salta el "Error" je

def calcular_suma():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        resultado = num1 + num2
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

def calcular_resta():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        resultado = num1 - num2
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

def calcular_multiplicacion():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        resultado = num1 * num2
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

def calcular_division():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        if num2 == 0:
            raise ZeroDivisionError #verifica si num2 es igual a cero. Si lo es, se lanza una excepción ZeroDivisionError para manejar el caso especial de la división por cero.
        resultado = num1 / num2
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')
    except ZeroDivisionError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

def calcular_porcentaje():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        resultado = (num1 * num2) / 100
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

def resetear():
    entrada_primero.delete(0, tk.END)
    entrada_segundo.delete(0, tk.END)
    entrada_resultado.config(state='normal')
    entrada_resultado.delete(0, tk.END)
    entrada_resultado.config(state='readonly')

root = tk.Tk()
root.title("Calculadora :3")

#ETIQUETAS

Primer_numero = tk.Label(root, text="Primer número", font=("Arial", 12), fg="black")
Primer_numero.grid(row=0, column=0, padx=20, pady=5, sticky="w")

entrada_primero = tk.Entry(root, font=("Arial", 12), width=16, state='normal')
entrada_primero.grid(row=0, column=1, padx=20, pady=5, sticky="w")

Segundo_numero = tk.Label(root, text="Segundo número", font=("Arial", 12), fg="black")
Segundo_numero.grid(row=1, column=0, padx=20, pady=5, sticky="w")

entrada_segundo = tk.Entry(root, font=("Arial", 12), width=16, state='normal')
entrada_segundo.grid(row=1, column=1, padx=20, pady=5, sticky="w")

Resultado = tk.Label(root, text="Resultado", font=("Arial", 12), fg="black")
Resultado.grid(row=2, column=0, padx=20, pady=5, sticky="w")

entrada_resultado = tk.Entry(root, font=("Arial", 12), width=16, state='readonly')
entrada_resultado.grid(row=2, column=1, padx=20, pady=5, sticky="w")

#BOTONES

boton_suma = tk.Button(root, text="+", font=("Comic Sans", 13), width=15, height=1, command=calcular_suma)
boton_suma.grid(row=3, column=0, padx=20, pady=15, sticky="w")

boton_resta = tk.Button(root, text="-", font=("Comic Sans", 13), width=15, height=1, command=calcular_resta)
boton_resta.grid(row=3, column=1, padx=20, pady=15, sticky="w")

boton_multiplicar = tk.Button(root, text="*", font=("Comic Sans", 13), width=15, height=1, command=calcular_multiplicacion)
boton_multiplicar.grid(row=4, column=0, padx=20, pady=5, sticky="w")

boton_dividir = tk.Button(root, text="/", font=("Comic Sans", 13), width=15, height=1, command=calcular_division)
boton_dividir.grid(row=4, column=1, padx=20, pady=5, sticky="w")

boton_porcentaje = tk.Button(root, text="%", font=("Comic Sans", 13), width=15, height=1, command=calcular_porcentaje)
boton_porcentaje.grid(row=5, column=0, padx=20, pady=10, sticky="w")

boton_reset = tk.Button(root, text="CLEAR", font=("Comic Sans", 13), width=15, height=1, command=resetear)
boton_reset.grid(row=5, column=1, padx=20, pady=10, sticky="w")

root.mainloop()