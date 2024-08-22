#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_11():
    
    def funcionCalcular():
        Area = float(txtnumero.get())*float(txtnumero.get())
        Perimetro = float(txtnumero.get())*4
        label_A.config(text=f"El área del cuadrado es: {Area}", font=("arial",12,"bold"))
        label_P.config(text=f"El perimetro del cuadrado es: {Perimetro}", font=("arial",12,"bold"))  
        
          
    ventana13 = tk.Tk()
    ventana13.title("EJERCICIO 11")
    ventana13.geometry("350x300")
    ventana13.resizable(False,False)
    ventana13.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana13,text="ÁREA&PERIMETRO", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Número
    label_numero = tk.Label(ventana13,text="Ingrese la medida del lado del cuadrado", font=("Arial",8,"bold"))
    label_numero.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Número escritura
    txtnumero = tk.Entry(ventana13,font=("Arial",8,"bold"))
    txtnumero.grid(row=2,column=0,padx=10,sticky="w")
    txtnumero.config(bg="#fff",font=("Arial",12),fg="black")
    #botón
    boton = tk.Button(ventana13, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionCalcular)
    boton.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    label_A = tk.Label(ventana13, text="Es: ", font=('Arial', 12))
    label_A.grid(row=4,column=0, padx=10,pady=10,sticky="w")
    
    label_P = tk.Label(ventana13, text="Es: ", font=('Arial', 12))
    label_P.grid(row=5,column=0, padx=10,pady=10,sticky="w")