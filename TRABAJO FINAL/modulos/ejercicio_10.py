#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_10():
    
    def funcionMostrar():
        if float(txtnumero.get()) == 1:
            label_B.config(text=f"Es el dia LUNES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 2:
            label_B.config(text=f"Es el dia MARTES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 3:
            label_B.config(text=f"Es el dia MIERCOLES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 4:
            label_B.config(text=f"Es el dia JUEVES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 5:
            label_B.config(text=f"Es el dia VIERNES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 6:
            label_B.config(text=f"Es el dia SABADO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 7:
            label_B.config(text=f"Es el dia DOMINGO", font=("arial",12,"bold"))
        else:
            label_B.config(text=f"No existe un día para ese número", font=("arial",12,"bold")) 
    
    ventana12 = tk.Tk()
    ventana12.title("EJERCICIO 10")
    ventana12.geometry("350x250")
    ventana12.resizable(False,False)
    ventana12.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana12,text="NÚMEROS&DÍAS", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Número
    label_numero = tk.Label(ventana12,text="Ingrese un número del 1 al 7", font=("Arial",8,"bold"))
    label_numero.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Número escritura
    txtnumero = tk.Entry(ventana12,font=("Arial",8,"bold"))
    txtnumero.grid(row=2,column=0,padx=10,sticky="w")
    txtnumero.config(bg="#fff",font=("Arial",12),fg="black")
    #botón
    boton = tk.Button(ventana12, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionMostrar)
    boton.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    label_B = tk.Label(ventana12, text="Es: ", font=('Arial', 12))
    label_B.grid(row=4,column=0, padx=10,pady=10,sticky="w")