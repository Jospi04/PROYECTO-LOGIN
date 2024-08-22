#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_12():
    def funcionConversion():
        TipoCambio = 3.75
        Conversion = float(txtdolar.get())* TipoCambio
        labelconversion.config(text=f"La cantidad convertida es de: {Conversion} Soles", font=("arial",12,"bold"))
        
        
    ventana14 = tk.Tk()
    ventana14.title("EJERCICIO 12")
    ventana14.geometry("400x250")
    ventana14.resizable(False,False)
    ventana14.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana14,text="CONVERSIÓN DÓLAR A SOLES", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=1,padx=10,pady=10)
    
    #Conversión
    label_dolar = tk.Label(ventana14,text="Ingrese la cantidad de dinero", font=("Arial",12,"bold"))
    label_dolar.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Conversión escritura
    txtdolar = tk.Entry(ventana14,font=("Arial",12,"bold"))
    txtdolar.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtdolar.config(bg="#fff",font=("Arial",12),fg="black")
    #Botón conversión
    boton_conversion = tk.Button(ventana14, text="CONVERTIR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionConversion)
    boton_conversion.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    labelconversion = tk.Label(ventana14, text="Es: ", font=('Arial', 12))
    labelconversion.grid(row=4,column=0, padx=10,pady=10,sticky="w")