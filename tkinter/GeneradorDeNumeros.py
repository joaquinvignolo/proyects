import tkinter as tk
import random

def generar_random():
    try:
        num1 = int(spinbox1.get())
        num2 = int(spinbox2.get())

        if num1 > num2:
            num1, num2 = num2, num1 #para que el primer valor no sea mayor al segundo
        
        #genera el numerito aleatorio
        numero_random = random.randint(num1, num2)

        entry_noedit.config(state='normal')
        entry_noedit.delete(0, tk.END)
        entry_noedit.insert(0, str(numero_random))
        entry_noedit.config(state='readonly')
    except ValueError: #para que el usuario no ingrese cosas raras (STRINGS!!!!!)
        entry_noedit.config(state='normal')
        entry_noedit.delete(0, tk.END)
        entry_noedit.insert(0, "Error")
        entry_noedit.config(state='readonly')

root = tk.Tk()
root.title("Generador de números")

num1 = tk.Label(root, text="Número 1", font=("Arial", 12), fg="black")
num1.grid(row=0, column=0, padx=20, pady=5, sticky="w")

num2 = tk.Label(root, text="Número 2", font=("Arial", 12), fg="black")
num2.grid(row=1, column=0, padx=20, pady=5, sticky="w")

num_gen = tk.Label(root, text="Número Generado", font=("Arial", 12), fg="black")
num_gen.grid(row=2, column=0, padx=20, pady=5, sticky="w")

entry_noedit = tk.Entry(root, font=("Arial", 12), width=10, state='readonly')
entry_noedit.grid(row=2, column=1, padx=20, pady=5, sticky="w")

spinbox1 = tk.Spinbox(root, from_=0, to=10, increment=1, font=("Arial", 12))
spinbox1.grid(row=0, column=1, padx=20, pady=5, sticky="w")

spinbox2 = tk.Spinbox(root, from_=0, to=10, increment=1, font=("Arial", 12))
spinbox2.grid(row=1, column=1, padx=20, pady=5, sticky="w")

boton_generar = tk.Button(root, text="Generar", font=("Arial", 12), width=9, height=1, command=generar_random)
boton_generar.grid(row=3, column=1, padx=20, pady=15, sticky="w")

root.mainloop()