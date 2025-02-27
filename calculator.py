import customtkinter as ctk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg="#2b2b2b")
        self.root.geometry("375x580")
        self.root.resizable(False, False)

        # Establecer tema y modo de apariencia
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Entrada
        self.entrada = ctk.CTkEntry(root, width=355, height=70, font=("Arial", 28), fg_color="#2b2b2b", text_color="white", justify="right", border_width=0, corner_radius=8)
        self.entrada.grid(row=0, column=0, columnspan=4, ipady=8, pady=(110, 5), padx=10)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('C', 2), ('←', 1), ('/', 1),
            ('7', 1), ('8', 1), ('9', 1), ('*', 1),
            ('4', 1), ('5', 1), ('6', 1), ('-', 1),
            ('1', 1), ('2', 1), ('3', 1), ('+', 1),
            ('0', 2), ('.', 1), ('=', 1)
        ]

        colores_botones = {
            'numero': '#4d4d4d',
            'operador': '#fe9505',
            'igual': '#fe9505',
            'fondo': '#2b2b2b',
            'texto': '#fff',
            'reset': '#d32f2f',
            'borrar': '#fe9505',
        }

        frame_botones = ctk.CTkFrame(self.root, fg_color=colores_botones['fondo'])
        frame_botones.grid(row=1, column=0, columnspan=5, pady=(10, 0), padx=5)

        fila = 0
        columna = 0

        for boton, span in botones:
            color_fondo = colores_botones['operador'] if boton in ['/','*','-','+','=','←'] else colores_botones['numero']
            if boton == 'C':
                color_fondo = colores_botones['reset']
            elif boton == '←':
                color_fondo = colores_botones['borrar']
            elif boton == '=':
                color_fondo = colores_botones['igual']

            button = ctk.CTkButton(frame_botones, text=boton, width=85 * span, height=60, font=("Arial", 20), fg_color=color_fondo, text_color=colores_botones['texto'], corner_radius=10, hover_color="#4bbfc1", command=lambda b=boton: self.click_boton(b))
            button.grid(row=fila, column=columna, columnspan=span, padx=2, pady=2, sticky='nsew')

            columna += span
            if columna >= 4:
                columna = 0
                fila += 1

        for i in range(4):
            frame_botones.grid_columnconfigure(i, weight=1)
        for i in range(fila + 1):
            frame_botones.grid_rowconfigure(i, weight=1)

    def click_boton(self, valor):
        if valor == "=":
            try:
                resultado = str(eval(self.entrada.get()))
                self.entrada.delete(0, "end")
                self.entrada.insert("end", resultado)
            except Exception:
                messagebox.showerror("Error", "Entrada no válida")
                self.entrada.delete(0, "end")
        elif valor == 'C':
            self.entrada.delete(0, "end")
        elif valor == '←':
            self.entrada.delete(len(self.entrada.get()) - 1, "end")
        else:
            self.entrada.insert("end", valor)

if __name__ == '__main__':
    root = ctk.CTk()
    calculadora = Calculadora(root)
    root.mainloop()