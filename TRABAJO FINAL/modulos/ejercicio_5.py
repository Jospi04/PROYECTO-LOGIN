#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_5():
    
    def funcionMostrar():
        signo = "aries"
        if signo == txtsigno.get() :
            label_S.config(text=f"Hola {txtnombre.get()}", font=("arial",12,"bold"))
        else:
            label_S.config(text=f"Hola no eres aries", font=("arial",12,"bold"))
        
    ventana7 = tk.Tk()
    ventana7.title("EJERCICIO 5")
    ventana7.geometry("330x330")
    ventana7.resizable(False,False)
    ventana7.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana7,text="NOMBRE&SIGNO", font=("Arial",15,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Nombre
    label_nombre = tk.Label(ventana7,text="Ingrese su nombre", font=("Arial",10,"bold"))
    label_nombre.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Nombre escritura
    txtnombre = tk.Entry(ventana7,font=("Arial",10,"bold"))
    txtnombre.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtnombre.config(bg="#fff",font=("Arial",12),fg="black")
    #Signo
    label_signo = tk.Label(ventana7,text="Ingrese su signo", font=("Arial",10,"bold"))
    label_signo.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #Signo escritura
    txtsigno = tk.Entry(ventana7,font=("Arial",10,"bold"))
    txtsigno.grid(row=4,column=0,columnspan=1,padx=10,sticky="w")
    txtsigno.config(bg="#fff",font=("Arial",12),fg="black")
    #Botón mostrar
    boton_signo = tk.Button(ventana7, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionMostrar)
    boton_signo.grid(row=5, column=0, padx=10,pady=10,sticky="w")
    
    label_S = tk.Label(ventana7, text="Es: ", font=('Arial', 12))
    label_S.grid(row=6,column=0, padx=10,pady=10,sticky="w")