import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tasks = []

        # Configuración de la interfaz gráfica
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Añadir Tarea", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", width=20, command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Eventos de teclas
        self.root.bind("<Return>", self.on_enter)  # Añadir tarea con Enter
        self.root.bind("<c>", self.on_complete)  # Marcar tarea como completada con "C"
        self.root.bind("<Delete>", self.on_delete)  # Eliminar tarea con "Delete"
        self.root.bind("<Escape>", self.on_escape)  # Cerrar aplicación con "Escape"

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["completed"] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")

    def on_enter(self, event):
        self.add_task()

    def on_complete(self, event):
        self.complete_task()

    def on_delete(self, event):
        self.delete_task()

    def on_escape(self, event):
        self.root.quit()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_display = task["task"]
            if task["completed"]:
                task_display += " (Completada)"
            self.task_listbox.insert(tk.END, task_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
