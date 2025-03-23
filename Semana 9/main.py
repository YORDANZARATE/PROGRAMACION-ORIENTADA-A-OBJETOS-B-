
# Función para agregar información a la lista
def agregar_info():
    info = entrada_texto.get()  # Obtiene el texto del campo de entrada
    if info:  # Verifica que no esté vacío
        lista_info.insert(tk.END, info)  # Agrega el texto a la lista
        entrada_texto.delete(0, tk.END)  # Borra el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese información.")

# Función para limpiar el campo de entrada o la lista
def limpiar_info():
    entrada_texto.delete(0, tk.END)  # Borra el campo de entrada
    lista_info.delete(0, tk.END)  # Borra toda lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Información")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=10)

# Campo de texto para ingresar información
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar información
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

# Lista para mostrar la información
lista_info = tk.Listbox(ventana, height=10, width=40)
lista_info.pack(pady=5)

# Botón para limpiar la información
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
