#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_3():
    
    def funcionMayor():
        primerN = float(txtprimern.get())
        segundoN = float(txtsegundon.get())
        tercerN = float(txttercern.get())
        if primerN > segundoN:
            messagebox.showinfo(title="MENSAJE", message="EL PRIMER NÚMERO ES EL MAYOR")
        elif segundoN > tercerN:
            messagebox.showinfo(title="MENSAJE", message="EL SEGUNDO NÚMERO ES EL MAYOR")
        else:
            messagebox.showinfo(title="MENSAJE", message="EL TERCER NÚMERO ES EL MAYOR")
    
    
    ventana5 = tk.Tk()
    ventana5.title("EJERCICIO 3")
    ventana5.geometry("330x350")
    ventana5.resizable(False,False)
    ventana5.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana5,text="INGRESE TRES NÚMEROS", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    
    #NOTA 1
    label_primern = tk.Label(ventana5,text="PRIMER NÚMERO", font=("Arial",8,"bold"))
    label_primern.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #NOTA 1 escritura
    txtprimern = tk.Entry(ventana5,font=("Arial",8,"bold"))
    txtprimern.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtprimern.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 2
    label_segundon = tk.Label(ventana5,text="SEGUNDO NÚMERO", font=("Arial",8,"bold"))
    label_segundon.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #NOTA 2 escritura
    txtsegundon = tk.Entry(ventana5,font=("Arial",8,"bold"))
    txtsegundon.grid(row=4,column=0,columnspan=1,padx=10,sticky="w")
    txtsegundon.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 3
    label_tercern = tk.Label(ventana5,text="TERCER NÚMERO", font=("Arial",8,"bold"))
    label_tercern.grid(row=5,column=0,padx=10,pady=10,sticky="w")
    #NOTA 3 escritura
    txttercern = tk.Entry(ventana5,font=("Arial",8,"bold"))
    txttercern.grid(row=6,column=0,columnspan=1,padx=10,sticky="w")
    txttercern.config(bg="#fff",font=("Arial",12),fg="black")
    
    #botón promedio
    boton_mayor = tk.Button(ventana5, text="SACAR EL MAYOR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionMayor)
    boton_mayor.grid(row=7, column=0, padx=10,pady=10,sticky="w")
    