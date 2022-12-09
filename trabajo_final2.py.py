from tkinter import *
from tkinter import ttk


ID = 0
# Defino las funciones para agregar y borrar autores
def fagregar():
    global ID
    ID += 1
    tree.insert("", "end", text=str(ID), values=(e_text1.get()))


def fborrar():
    global ID
    item = tree.focus()
    tree.delete(item)
    ID -= 1


# Defino la ventana principal de la aplicación
root = Tk()

# Defino las variables que voy a usar
Nombre1 = StringVar()


# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title("Base de datos de Genes")

# Creo las etiquetas y los botones
l_Nombre1 = ttk.Label(root, text="Gen: ")


e_text1 = ttk.Entry(root, textvariable=Nombre1, width=15)

# Menu de opciones de búsqueda
menub = Menubutton(root, text="Búsqueda", activebackground="blue")
menub.grid()
menub.menu = Menu(menub, tearoff=0)
menub["menu"] = menub.menu
opcion1 = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()
opcion4 = IntVar()
opcion5 = IntVar()
opcion6 = IntVar()
opcion7 = IntVar()
menub.menu.add_checkbutton(label="Nombre aprobado", variable=opcion1)
menub.menu.add_checkbutton(label="Cromosoma", variable=opcion2)
menub.menu.add_checkbutton(label="OMIM ID", variable=opcion3)
menub.menu.add_checkbutton(label="UniProt ID", variable=opcion4)
menub.menu.add_checkbutton(label="Tipo de locus", variable=opcion5)
menub.menu.add_checkbutton(label="MANE select Ensembl transcript ID", variable=opcion6)
menub.menu.add_checkbutton(label="MANE Select RefSeq transcript ID", variable=opcion7)

b_borrar = ttk.Button(root, text="Borrar", command=fborrar)
b_salir = ttk.Button(root, text="Salir", command=root.quit)

tree = ttk.Treeview(root)
tree["columns"] = "col1"
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80)


# Posiciono los controles
l_Nombre1.grid(column=0, row=0)
e_text1.grid(column=1, row=0)
tree.grid(column=0, row=3, columnspan=4)  # el output
menub.grid(column=3, row=0)
b_borrar.grid(column=3, row=1)
b_salir.grid(column=3, row=5)


mainloop()
