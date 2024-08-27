import tkinter as tk
import math

def calcular_factorial():
    
    global numero   
    resultado = math.factorial(numero)
        
    campo_entrada_resultado.config(state='normal') 
    campo_entrada_resultado.delete(0, tk.END)  
    campo_entrada_resultado.insert(0, str(resultado)) 
    campo_entrada_resultado.config(state='readonly')  
        
    numero += 1
        
    campo_entrada_numero.config(state='normal')
    campo_entrada_numero.delete(0, tk.END)
    campo_entrada_numero.insert(0, str(numero))
    campo_entrada_numero.config(state='readonly')

root = tk.Tk()
root.title("Factorial")

numero = 1

etiqueta_numero = tk.Label(root, text="Número (n):", font=("Arial", 12))
etiqueta_numero.pack(padx=20, pady=5, side=tk.LEFT)

campo_entrada_numero = tk.Entry(root, font=("Arial", 12), width=10, state='readonly')
campo_entrada_numero.pack(padx=10, pady=5, side=tk.LEFT)
campo_entrada_numero.insert(0, str(numero))

etiqueta_resultado = tk.Label(root, text="Factorial(n):", font=("Arial", 12))
etiqueta_resultado.pack(padx=20, pady=5, side=tk.LEFT)

campo_entrada_resultado = tk.Entry(root, font=("Arial", 12), width=10, state='readonly')
campo_entrada_resultado.pack(padx=10, pady=5, side=tk.LEFT)

boton_calcular = tk.Button(
    root,
    text="Siguiente",
    command=calcular_factorial,
    font=("Arial", 12)
)
boton_calcular.pack(padx=20, pady=20)

root.mainloop()