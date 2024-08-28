import tkinter as tk
from tkinter import messagebox

def aniadir_pelicula():
    
    pelicula = entry_peli.get().strip()  #el strip elimina los espacios en blanco para no ingresar espacios vacios
    
    if pelicula:  
        listbox.insert(tk.END, pelicula)
        entry_peli.delete(0, tk.END)  #añade el texto y limpia la entrada
    else:
        tk.messagebox.showwarning("Error")
        entry_peli.delete(0, tk.END)

root = tk.Tk()
root.title("Películas")

Etiq_1 = tk.Label(root, text="Escribe el título de una película", font=("Arial", 12), fg="black")
Etiq_1.grid(row=0, column=0, padx=20, pady=5, sticky="w")

Etiq_2 = tk.Label(root, text="Películas", font=("Arial", 12), fg="black")
Etiq_2.grid(row=0, column=1, padx=20, pady=5, sticky="w")

entry_peli = tk.Entry(root, font=("Arial", 12), width=23, state='normal')
entry_peli.grid(row=1, column=0, padx=20, pady=5, sticky="w")

boton_aniadir = tk.Button(root, text="Añadir", font=("Arial", 12), width=23, height=1, command=aniadir_pelicula)
boton_aniadir.grid(row=2, column=0, padx=20, pady=15, sticky="w")

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
listbox.grid(row=1, column=1, rowspan=2, padx=20, pady=5, sticky="n")

root.mainloop()