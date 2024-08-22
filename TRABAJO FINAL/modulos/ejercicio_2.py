#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_2():
    
    def funcionConversion():
        Gradocelcius = float(txtcelcius.get())
        Conversion = (9/5)*Gradocelcius+32
        labelconversion.config(text=f"EL GRADO FAHRENHEIT ES: {Conversion}", font=("arial",12,"bold"))
        
        
        
        
        
    ventana4 = tk.Tk()
    ventana4.title("EJERCICIO 2")
    ventana4.geometry("350x300")
    ventana4.resizable(False,False)
    ventana4.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana4,text="CONVERSIÓN DE GRADOS", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    
    #GRADO C
    label_Celsius = tk.Label(ventana4,text="Ingrese el grado Celsius", font=("Arial",12,"bold"))
    label_Celsius.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #GRADO C escritura
    txtcelcius = tk.Entry(ventana4,font=("Arial",12,"bold"))
    txtcelcius.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtcelcius.config(bg="#fff",font=("Arial",12),fg="black")
    #Botón conversión
    boton_conversion = tk.Button(ventana4, text="CONVERTIR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionConversion)
    boton_conversion.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    labelconversion = tk.Label(ventana4, text="Es: ", font=('Arial', 12))
    labelconversion.grid(row=4,column=0, padx=10,pady=10,sticky="w")