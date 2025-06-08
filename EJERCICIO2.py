import tkinter as tk
from tkinter import messagebox
import math


class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_superficie(self, superficie):
        self.superficie = superficie

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)

    def calcular_superficie(self):
        area_lado_a = 2 * math.pi * self.radio * self.altura
        area_lado_b = 2 * math.pi * (self.radio ** 2)
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4 / 3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lado = 2 * self.base * self.apotema
        return area_base + area_lado



class VentanaCilindro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("280x210")
        self.create_widgets()

    def create_widgets(self):
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.pack()

        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.pack()

        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm³):")
        self.volumen_label.pack()

        self.superficie_label = tk.Label(self, text="Superficie (cm²):")
        self.superficie_label.pack()

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)

            self.volumen_label.config(text=f"Volumen (cm³): {cilindro.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm²): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


class VentanaEsfera(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("280x200")
        self.create_widgets()

    def create_widgets(self):
        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.pack()

        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm³):")
        self.volumen_label.pack()

        self.superficie_label = tk.Label(self, text="Superficie (cm²):")
        self.superficie_label.pack()

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            esfera = Esfera(radio)

            self.volumen_label.config(text=f"Volumen (cm³): {esfera.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm²): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


class VentanaPiramide(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("280x240")
        self.create_widgets()

    def create_widgets(self):
        self.base_label = tk.Label(self, text="Base (cms):")
        self.base_label.pack()

        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.pack()

        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        self.apotema_label = tk.Label(self, text="Apotema (cms):")
        self.apotema_label.pack()

        self.apotema_entry = tk.Entry(self)
        self.apotema_entry.pack()

        self.calcular_button = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm³):")
        self.volumen_label.pack()

        self.superficie_label = tk.Label(self, text="Superficie (cm²):")
        self.superficie_label.pack()

    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            piramide = Piramide(base, altura, apotema)

            self.volumen_label.config(text=f"Volumen (cm³): {piramide.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm²): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x160")
        self.create_widgets()

    def create_widgets(self):
        self.cilindro_button = tk.Button(self, text="Cilindro", command=self.ventana_cilindro)
        self.cilindro_button.pack(pady=10)

        self.esfera_button = tk.Button(self, text="Esfera", command=self.ventana_esfera)
        self.esfera_button.pack(pady=10)

        self.piramide_button = tk.Button(self, text="Pirámide", command=self.ventana_piramide)
        self.piramide_button.pack(pady=10)

    def ventana_cilindro(self):
        ventana = VentanaCilindro()
        ventana.mainloop()

    def ventana_esfera(self):
        ventana = VentanaEsfera()
        ventana.mainloop()

    def ventana_piramide(self):
        ventana = VentanaPiramide()
        ventana.mainloop()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
