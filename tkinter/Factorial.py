import tkinter as tk
from tkinter import messagebox
import math

def calcular_factorial():
    global numero
    
    # Calcular el factorial
    try:
        # Calcular el factorial del número actual
        resultado = math.factorial(numero)
        
        # Mostrar el resultado en el campo de entrada de resultado
        campo_entrada_resultado.config(state='normal')  # Hacer editable temporalmente
        campo_entrada_resultado.delete(0, tk.END)  # Eliminar el texto actual
        campo_entrada_resultado.insert(0, str(resultado))  # Insertar el nuevo valor
        campo_entrada_resultado.config(state='readonly')  # Volver a hacer readonly
        
        # Incrementar el número para la próxima vez
        numero += 1
        
        # Actualizar el campo de entrada de número con el nuevo valor
        campo_entrada_numero.config(state='normal')  # Hacer editable temporalmente
        campo_entrada_numero.delete(0, tk.END)  # Eliminar el texto actual
        campo_entrada_numero.insert(0, str(numero))  # Insertar el nuevo valor
        campo_entrada_numero.config(state='readonly')  # Volver a hacer readonly
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Factorial")

# Inicializar el número
numero = 1

# Crear una etiqueta para el número
etiqueta_numero = tk.Label(root, text="Número (n):", font=("Comic Sans", 11))
etiqueta_numero.pack(padx=20, pady=5, side=tk.LEFT)

# Crear un campo de entrada para el número, inicialmente no editable
campo_entrada_numero = tk.Entry(root, font=("Comic Sans", 11), width=10, state='readonly')
campo_entrada_numero.pack(padx=10, pady=5, side=tk.LEFT)
campo_entrada_numero.insert(0, str(numero))  # Inicializar el campo con el valor del número

# Crear una etiqueta para el resultado
etiqueta_resultado = tk.Label(root, text="Factorial(n):", font=("Comic Sans", 11))
etiqueta_resultado.pack(padx=20, pady=5, side=tk.LEFT)

# Crear un campo de entrada para el resultado, no editable
campo_entrada_resultado = tk.Entry(root, font=("Comic Sans", 11), width=10, state='readonly')
campo_entrada_resultado.pack(padx=10, pady=5, side=tk.LEFT)

# Crear un botón para calcular el factorial
boton_calcular = tk.Button(
    root,
    text="Siguiente",
    command=calcular_factorial,
    font=("Comic Sans", 11)
)
boton_calcular.pack(padx=20, pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()