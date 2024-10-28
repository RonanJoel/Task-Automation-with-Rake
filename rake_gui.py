import tkinter as tk
from tkinter import messagebox
import subprocess

class TaskAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatización de Tareas con Rake")
        self.root.geometry("500x400")
        
        # Variables de tema
        self.current_theme = "light"
        self.themes = {
            "light": {"bg": "#f0f0f0", "fg": "#000000", "button_bg": "#4CAF50"},
            "dark": {"bg": "#333333", "fg": "#ffffff", "button_bg": "#555555"}
        }
        
        # Menú de temas
        menu_bar = tk.Menu(root)
        task_menu = tk.Menu(menu_bar, tearoff=0)
        task_menu.add_command(label="Ejecutar Tarea Ejemplo", command=self.ejecutar_tarea)
        task_menu.add_separator()
        task_menu.add_command(label="Salir", command=root.quit)
        menu_bar.add_cascade(label="Tareas", menu=task_menu)

        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_command(label="Claro", command=lambda: self.cambiar_tema("light"))
        theme_menu.add_command(label="Oscuro", command=lambda: self.cambiar_tema("dark"))
        menu_bar.add_cascade(label="Tema", menu=theme_menu)
        root.config(menu=menu_bar)
        
        # Botón para ejecutar tarea
        self.ejecutar_button = tk.Button(root, text="Ejecutar Tarea", command=self.ejecutar_tarea)
        self.ejecutar_button.pack(pady=10)

        # Área de texto para mostrar resultados
        self.output_text = tk.Text(root, width=50, height=15, wrap=tk.WORD)
        self.output_text.pack(pady=10)

        # Aplicar tema inicial
        self.cambiar_tema(self.current_theme)

    def ejecutar_tarea(self):
        """Ejecuta una tarea de Rake y muestra el resultado en el área de texto."""
        try:
            resultado = subprocess.run(['rake', 'my_tasks:example_task'], capture_output=True, text=True)
            if resultado.returncode != 0:
                raise Exception(resultado.stderr.strip())
            self.output_text.insert(tk.END, resultado.stdout + "\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cambiar_tema(self, theme):
        """Cambia el tema de la aplicación."""
        self.current_theme = theme
        colors = self.themes[theme]
        self.root.configure(bg=colors["bg"])
        self.output_text.configure(bg=colors["bg"], fg=colors["fg"])
        self.ejecutar_button.configure(bg=colors["button_bg"], fg=colors["fg"])

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskAutomationApp(root)
    root.mainloop()



