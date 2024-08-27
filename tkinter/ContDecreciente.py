import tkinter as tk

def actualizar_contador():
    global contador
    contador -= 1
    entry.config(state='normal') #editable
    entry.delete(0, tk.END)
    entry.insert(0, str(contador))
    entry.config(state='readonly') #no editable

root = tk.Tk()
root.title("ContDecreciente") #título

contador = 88 #variable contador arranca en 88

etiqueta = tk.Label(root, text="Contador", font=("Comic Sans", 14), fg="red")
etiqueta.pack(padx=20, pady=5, side=tk.LEFT) #el label que muestra contador

entry = tk.Entry(root, font=("Comic Sans", 11), width=10, state='readonly')
entry.pack(padx=10, pady=5, side=tk.LEFT) #el entry no editable

entry.insert(0, str(contador)) #convierto a string la variable contador y la inserto en el entry

button = tk.Button(
    root,
    text="-",
    command=actualizar_contador,
    font=("Comic Sans", 15),
    width=3,
    height=1
)
button.pack(padx=20, pady=20)

root.mainloop()