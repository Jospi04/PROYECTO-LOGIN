#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import math

def abrirventanaejercicio_7():
    
    def funcionResultados():
        Num1 = float(txtnumero1.get())
        Num2 = float(txtnumero2.get())
        Num3 = float(txtnumero3.get())
        Num4 = float(txtnumero4.get())
        Num5 = float(txtnumero5.get())
        Suma = Num1+Num4
        Multiplicacion = Num2*Num5
        Raiz = math.sqrt(Num3)
        label_S.config(text=f"El resultado de la suma es: {Suma}", font=("arial",12,"bold"))
        label_M.config(text=f"El resultado de la multiplicación es: {Multiplicacion}", font=("arial",12,"bold"))
        label_R.config(text=f"El resultado de la raíz es: {Raiz}", font=("arial",12,"bold"))
        
    ventana9 = tk.Tk()
    ventana9.title("EJERCICIO 7")
    ventana9.geometry("450x650")
    ventana9.resizable(False,False)
    ventana9.iconbitmap("icons/favicon.ico")
    #Titulo del Ejercicio
    label_titulo = tk.Label(ventana9,text="OPERACIONES MATEMATICAS", font=("Arial",15,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Número 1
    label_numero1 = tk.Label(ventana9,text="Número 1", font=("Arial",10,"bold"))
    label_numero1.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Número 1 escritura
    txtnumero1 = tk.Entry(ventana9,font=("Arial",10,"bold"))
    txtnumero1.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtnumero1.config(bg="#fff",font=("Arial",12),fg="black")
    #Número 2
    label_numero2 = tk.Label(ventana9,text="Número 2", font=("Arial",10,"bold"))
    label_numero2.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #Número 2 escritura
    txtnumero2= tk.Entry(ventana9,font=("Arial",10,"bold"))
    txtnumero2.grid(row=4,column=0,columnspan=1,padx=10,sticky="w")
    txtnumero2.config(bg="#fff",font=("Arial",12),fg="black")
    #Número 3
    label_numero3 = tk.Label(ventana9,text="Número 3", font=("Arial",10,"bold"))
    label_numero3.grid(row=5,column=0,padx=10,pady=10,sticky="w")
    #Número 3 escritura
    txtnumero3 = tk.Entry(ventana9,font=("Arial",10,"bold"))
    txtnumero3.grid(row=6,column=0,columnspan=1,padx=10,sticky="w")
    txtnumero3.config(bg="#fff",font=("Arial",12),fg="black")
    #Número 4
    label_numero4 = tk.Label(ventana9,text="Número 4", font=("Arial",10,"bold"))
    label_numero4.grid(row=7,column=0,padx=10,pady=10,sticky="w")
    #Número 4 escritura
    txtnumero4 = tk.Entry(ventana9,font=("Arial",10,"bold"))
    txtnumero4.grid(row=8,column=0,columnspan=1,padx=10,sticky="w")
    txtnumero4.config(bg="#fff",font=("Arial",12),fg="black")
    ##Número 5
    label_numero5 = tk.Label(ventana9,text="Número 5", font=("Arial",10,"bold"))
    label_numero5.grid(row=9,column=0,padx=10,pady=10,sticky="w")
    #Número 5 escritura
    txtnumero5 = tk.Entry(ventana9,font=("Arial",10,"bold"))
    txtnumero5.grid(row=10,column=0,columnspan=1,padx=10,sticky="w")
    txtnumero5.config(bg="#fff",font=("Arial",12),fg="black")
    #botón
    boton = tk.Button(ventana9, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionResultados)
    boton.grid(row=11, column=0, padx=10,pady=10,sticky="w")
    
    label_S = tk.Label(ventana9, text="Es: ", font=('Arial', 12))
    label_S.grid(row=12,column=0, padx=10,pady=10,sticky="w")
    
    label_M = tk.Label(ventana9, text="Es: ", font=('Arial', 12))
    label_M.grid(row=13,column=0, padx=10,pady=10,sticky="w")
    
    label_R = tk.Label(ventana9, text="Es: ", font=('Arial', 12))
    label_R.grid(row=14,column=0, padx=10,pady=10,sticky="w")