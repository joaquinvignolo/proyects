import tkinter as tk

def incrementa_contador():
    global contador
    contador += 1
    entry.config(state='normal') #editable
    entry.delete(0, tk.END)
    entry.insert(0, str(contador))
    entry.config(state='readonly') #no editable
    
def decrece_contador():
    global contador
    contador -= 1
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.insert(0, str(contador))
    entry.config(state='readonly')
    
def resetear():
    global contador
    contador = 0
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.insert(0, str(contador))
    entry.config(state='readonly')
root = tk.Tk()
root.title("Contador")

contador = 0 #variable contador arranca en 0

etiqueta = tk.Label(root, text="Contador", font=("Comic Sans", 14), fg="red")
etiqueta.pack(padx=20, pady=5, side=tk.LEFT) #el label que muestra contador

entry = tk.Entry(root, font=("Comic Sans", 11), width=10, state='readonly')
entry.pack(padx=10, pady=5, side=tk.LEFT) #el entry no editable

entry.insert(0, str(contador)) #convierto a string la variable contador y la inserto en el entry

button_up = tk.Button(
    root,
    text="Count up",
    command=incrementa_contador,
    font=("Comic Sans", 12),
    width=9,
    height=1
)
button_up.pack(padx=20, pady=20, side=tk.LEFT)

button_down = tk.Button(
    root,
    text="Count down",
    command=decrece_contador,
    font=("Comic Sans", 12),
    width=9,
    height=1
)
button_down.pack(padx=20, pady=20, side=tk.LEFT)

reset = tk.Button(
    root,
    text="Reset",
    command=resetear,
    font=("Comic Sans", 12),
    width=9,
    height=1
)
reset.pack(padx=20, pady=20, side=tk.LEFT)

root.mainloop()