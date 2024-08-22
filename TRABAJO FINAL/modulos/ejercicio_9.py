#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_9():
    
    def funcionMostrar():
        
        if float(txtnumero.get()) == 0:
           label_B.config(text=f"ES CERO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 1:
             label_B.config(text=f"ES UNO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 2:
            label_B.config(text=f"ES DOS", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 3:
            label_B.config(text=f"ES TRES", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 4:
            label_B.config(text=f"ES CUATRO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 5:
            label_B.config(text=f"ES CINCO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 6:
            label_B.config(text=f"ES SEIS", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 7:
            label_B.config(text=f"ES SIETE", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 8:
            label_B.config(text=f"ES OCHO", font=("arial",12,"bold"))
        elif float(txtnumero.get()) == 9:
            label_B.config(text=f"ES NUEVE", font=("arial",12,"bold"))
        elif float(txtnumero.get()) >=10:
            label_B.config(text=f"ES UN NUMERO DE DOS DIGITOS", font=("arial",12,"bold"))
        
    ventana11 = tk.Tk()
    ventana11.title("EJERCICIO 9")
    ventana11.geometry("350x350")
    ventana11.resizable(False,False)
    ventana11.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana11,text="NÚMEROS", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Número
    label_numero = tk.Label(ventana11,text="Ingrese un número de un digito", font=("Arial",8,"bold"))
    label_numero.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Número escritura
    txtnumero = tk.Entry(ventana11,font=("Arial",8,"bold"))
    txtnumero.grid(row=2,column=0,padx=10,sticky="w")
    txtnumero.config(bg="#fff",font=("Arial",12),fg="black")
    #botón
    boton = tk.Button(ventana11, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionMostrar)
    boton.grid(row=3, column=0, padx=10,pady=10,sticky="w")
    
    label_B = tk.Label(ventana11, text="Es: ", font=('Arial', 12))
    label_B.grid(row=4,column=0, padx=10,pady=10,sticky="w")