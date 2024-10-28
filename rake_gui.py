import tkinter as tk
from tkinter import messagebox
import subprocess

class TaskAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatización de Tareas con Rake")
        
     
        self.root.configure(bg="#f0f0f0")
        

        menu_bar = tk.Menu(root)
        task_menu = tk.Menu(menu_bar, tearoff=0)
        task_menu.add_command(label="Ejecutar Tarea Ejemplo", command=self.ejecutar_tarea)
        task_menu.add_separator()
        task_menu.add_command(label="Salir", command=root.quit)
        menu_bar.add_cascade(label="Tareas", menu=task_menu)
        root.config(menu=menu_bar)


        self.ejecutar_button = tk.Button(root, text="Ejecutar Tarea", command=self.ejecutar_tarea, bg="#4CAF50", fg="white")
        self.ejecutar_button.pack(pady=10)

        self.output_text = tk.Text(root, width=50, height=15, bg="#ffffff", fg="#000000", wrap=tk.WORD)
        self.output_text.pack(pady=10)

    def ejecutar_tarea(self):
        try:
    
            resultado = subprocess.run(['rake', 'my_tasks:example_task'], capture_output=True, text=True)
            if resultado.returncode != 0:
                raise Exception(resultado.stderr.strip())
            self.output_text.insert(tk.END, resultado.stdout + "\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskAutomationApp(root)
    root.mainloop()

