import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    
    def __init__(self):
        self.lista_notas = [0.0] * 5  
    
    def calcular_promedio(self):

        suma = 0
        for i in range(len(self.lista_notas)): 
            suma += self.lista_notas[i]  
        

        return suma / len(self.lista_notas)
    
    def calcular_desviacion(self):

        prom = self.calcular_promedio()
        suma = 0
        for i in range(len(self.lista_notas)):
            suma += (self.lista_notas[i] - prom) ** 2
        
        
        return math.sqrt(suma / len(self.lista_notas))
    
    def calcular_menor(self):

        menor = self.lista_notas[0]
        for i in range(len(self.lista_notas)):
            if self.lista_notas[i] < menor:
                menor = self.lista_notas[i]
        return menor
    
    def calcular_mayor(self):

        mayor = self.lista_notas[0]  
        for i in range(len(self.lista_notas)): 
            if self.lista_notas[i] > mayor:

                mayor = self.lista_notas[i]
        return mayor


class VentanaPrincipal:
    
    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Notas")  
        self.ventana.geometry("280x380")  
        self.ventana.resizable(False, False)  
        
        
        self.ventana.eval('tk::PlaceWindow . center')
        
        
        self.inicializar_componentes()
    
    def inicializar_componentes(self):

        tk.Label(self.ventana, text="Nota 1:").place(x=20, y=20, width=80, height=23)
        self.campo_nota1 = tk.Entry(self.ventana)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)
        
        tk.Label(self.ventana, text="Nota 2:").place(x=20, y=50, width=80, height=23)
        self.campo_nota2 = tk.Entry(self.ventana)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)
        
        tk.Label(self.ventana, text="Nota 3:").place(x=20, y=80, width=80, height=23)
        self.campo_nota3 = tk.Entry(self.ventana)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)
        
        tk.Label(self.ventana, text="Nota 4:").place(x=20, y=110, width=80, height=23)
        self.campo_nota4 = tk.Entry(self.ventana)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)
        
        tk.Label(self.ventana, text="Nota 5:").place(x=20, y=140, width=80, height=23)
        self.campo_nota5 = tk.Entry(self.ventana)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)
        
        
        self.boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=20, y=170, width=100, height=23)
        
        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=125, y=170, width=80, height=23)
        
        
        self.etiqueta_promedio = tk.Label(self.ventana, text="Promedio = ")
        self.etiqueta_promedio.place(x=20, y=210, width=240, height=23)
        
        self.etiqueta_desviacion = tk.Label(self.ventana, text="Desviación = ")
        self.etiqueta_desviacion.place(x=20, y=240, width=240, height=23)
        
        self.etiqueta_mayor = tk.Label(self.ventana, text="Nota mayor = ")
        self.etiqueta_mayor.place(x=20, y=270, width=240, height=23)
        
        self.etiqueta_menor = tk.Label(self.ventana, text="Nota menor = ")
        self.etiqueta_menor.place(x=20, y=300, width=240, height=23)
    
    def calcular(self):

        try:
            
            notas = Notas()
    
            notas.lista_notas[0] = float(self.campo_nota1.get())
            notas.lista_notas[1] = float(self.campo_nota2.get())
            notas.lista_notas[2] = float(self.campo_nota3.get())
            notas.lista_notas[3] = float(self.campo_nota4.get())
            notas.lista_notas[4] = float(self.campo_nota5.get())
            
            promedio = notas.calcular_promedio()
            desviacion = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()
            
            self.etiqueta_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.etiqueta_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.etiqueta_mayor.config(text=f"Valor mayor = {mayor:.2f}")
            self.etiqueta_menor.config(text=f"Valor menor = {menor:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos en todos los campos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def limpiar(self):

        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)
        
        
        self.etiqueta_promedio.config(text="Promedio = ")
        self.etiqueta_desviacion.config(text="Desviación = ")
        self.etiqueta_mayor.config(text="Nota mayor = ")
        self.etiqueta_menor.config(text="Nota menor = ")
    
    def mostrar(self):
        self.ventana.mainloop()


def main():
    ventana_principal = VentanaPrincipal()
    ventana_principal.mostrar()


if __name__ == "__main__":
    main()
    
