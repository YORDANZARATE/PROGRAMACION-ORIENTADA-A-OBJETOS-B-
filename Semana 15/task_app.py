import tkinter as tk
from tkinter import messagebox

#   Esta Función es para añadir tareas

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

#  Esta Función es para marcar una tarea como completada

def complete_task():
    try:
        selected_task = listbox.curselection()
        task = listbox.get(selected_task)
        # Cambiar el color de la tarea para marcarla como completada
        listbox.itemconfig(selected_task, {'bg': 'lightgreen'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Función para permitir añadir tareas al presionar Enter
def enter_pressed(event):
    add_task()

# Creamos una  ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Creamos widgets

entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
complete_button = tk.Button(root, text="Marcar como Completada", width=20, command=complete_task)
delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
listbox = tk.Listbox(root, width=50, height=10)

# Enlazar tecla Enter para añadir tarea
root.bind('<Return>', enter_pressed)

# Ubicar los widgets
entry.pack(pady=10)
add_button.pack(pady=5)
complete_button.pack(pady=5)
delete_button.pack(pady=5)
listbox.pack(pady=10)

# Ejecutamos  la aplicación

root.mainloop()
