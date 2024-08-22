#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_4():
    
    def funcionDesceunto():
        compra = float(txtcompra.get())
        descuento = (15/100)*compra
        preciofinal = compra-descuento
        labeldescuento.config(text=f"El precio Final es de {preciofinal} soles", font=("arial",12,"bold"))
        
    
    ventana6 = tk.Tk()
    ventana6.title("EJERCICIO 4")
    ventana6.geometry("330x300")
    ventana6.resizable(False,False)
    ventana6.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana6,text="DESCUENTO DEL 15%", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #COMPRA
    label_compra = tk.Label(ventana6,text="Ingrese el total de la compra", font=("Arial",8,"bold"))
    label_compra.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #COMPRA escritura
    txtcompra = tk.Entry(ventana6,font=("Arial",8,"bold"))
    txtcompra.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtcompra.config(bg="#fff",font=("Arial",12),fg="black")
    #botón descuento
    boton_descuento = tk.Button(ventana6, text="APLICAR DESCUENTO", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionDesceunto)
    boton_descuento.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    labeldescuento = tk.Label(ventana6, text="Es: ", font=('Arial', 12))
    labeldescuento.grid(row=4,column=0, padx=10,pady=10,sticky="w")