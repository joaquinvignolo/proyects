import tkinter as tk 

root = tk.Tk()
root.title("Calculadora 2")

#FUNCIONES

def calcular():
    try:
        num1 = float(entrada_primero.get())
        num2 = float(entrada_segundo.get())
        operacion = variable_operacion.get()

        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida")

        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, str(resultado))
        entrada_resultado.config(state='readonly')

    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')
    except ZeroDivisionError: #como explique en la anterior calculadora no se puede dividir un numero al 0 entonces llamo al manejo de error para este caso
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error")
        entrada_resultado.config(state='readonly')

#ETIQUETAS

Valor1 = tk.Label(root, text="Valor 1", font=("Arial", 12), fg="black")
Valor1.grid(row=1, column=0, padx=20, pady=5, sticky="w")

entrada_primero = tk.Entry(root, font=("Arial", 12), width=16, state='normal')
entrada_primero.grid(row=1, column=1, padx=20, pady=5, sticky="w")

Valor2 = tk.Label(root, text="Valor 2", font=("Arial", 12), fg="black")
Valor2.grid(row=2, column=0, padx=20, pady=5, sticky="w")

entrada_segundo = tk.Entry(root, font=("Arial", 12), width=16, state='normal')
entrada_segundo.grid(row=2, column=1, padx=20, pady=5, sticky="w")

Resultado = tk.Label(root, text="Resultado", font=("Arial", 12), fg="black")
Resultado.grid(row=3, column=0, padx=20, pady=5, sticky="w")

entrada_resultado = tk.Entry(root, font=("Arial", 12), width=16, state='readonly')
entrada_resultado.grid(row=3, column=1, padx=20, pady=5, sticky="w")

Operaciones = tk.Label(root, text="Operaciones", font=("Arial", 12), fg="black")
Operaciones.grid(row=0, column=2, padx=20, pady=5, sticky="w")

#BOTONES

variable_operacion = tk.StringVar()
variable_operacion.set("Sumar")  # Valor predeterminado

boton_suma = tk.Radiobutton(root, text="Sumar", variable=variable_operacion, value="Sumar", font=("Comic Sans", 13))
boton_suma.grid(row=1, column=2, padx=20, pady=10, sticky="w")

boton_resta = tk.Radiobutton(root, text="Restar", variable=variable_operacion, value="Restar", font=("Comic Sans", 13))
boton_resta.grid(row=2, column=2, padx=20, pady=5, sticky="w")

boton_multiplicar = tk.Radiobutton(root, text="Multiplicar", variable=variable_operacion, value="Multiplicar", font=("Comic Sans", 13))
boton_multiplicar.grid(row=3, column=2, padx=20, pady=5, sticky="w")

boton_dividir = tk.Radiobutton(root, text="Dividir", variable=variable_operacion, value="Dividir", font=("Comic Sans", 13))
boton_dividir.grid(row=4, column=2, padx=20, pady=10, sticky="w")

boton_calcular = tk.Button(root, text="Calcular", font=("Comic Sans", 13), command=calcular)
boton_calcular.grid(row=5, column=2, padx=20, pady=10, sticky="w")

root.mainloop()