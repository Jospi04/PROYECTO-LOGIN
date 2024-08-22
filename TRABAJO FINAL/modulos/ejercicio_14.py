#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox


def abrirventanaejercicio_14():
    
    def funcionResultado():
        Edad = float(txtedad.get())
        Puntaje = float(txtpuntaje.get())
        if Edad >=18 and Puntaje >= 90:
            label_M.config(text=f"Premio de primer lugar en la categoria Adulta. :)", font=("arial",12,"bold"))
        elif Edad <=17 and Puntaje >= 90:
            label_M.config(text=f"Premio de primer lugar en la categoria juvenil. :) ", font=("arial",12,"bold"))
        elif Edad >=18 and Puntaje >= 70:
            label_M.config(text=f"Mención honorifica en la categoria adulta. :)", font=("arial",12,"bold"))
        elif Edad <=17 and Puntaje >= 70:
            label_M.config(text=f"Mención honorifica en la categoria juvenil. :)", font=("arial",12,"bold"))
        elif Edad <=17 and Puntaje <= 69:
            label_M.config(text=f"No recibe premios", font=("arial",12,"bold"))
        elif Edad >=18 and Puntaje <= 69:
            label_M.config(text=f"No recibe premios", font=("arial",12,"bold"))
    
    ventana16 = tk.Tk()
    ventana16.title("EJERCICIO 14")
    ventana16.geometry("450x310")
    ventana16.resizable(False,False)
    ventana16.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana16,text="PREMIACIÓN", font=("Arial",15,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Edad
    label_edad = tk.Label(ventana16,text="Ingrese su edad", font=("Arial",10,"bold"))
    label_edad.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Edad escritura
    txtedad = tk.Entry(ventana16,font=("Arial",10,"bold"))
    txtedad.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtedad.config(bg="#fff",font=("Arial",12),fg="black")
    #Pumtaje
    label_puntaje = tk.Label(ventana16,text="Ingrese su Puntaje", font=("Arial",10,"bold"))
    label_puntaje.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #Puntaje escritura
    txtpuntaje = tk.Entry(ventana16,font=("Arial",10,"bold"))
    txtpuntaje.grid(row=4,column=0,columnspan=1,padx=10,sticky="w")
    txtpuntaje.config(bg="#fff",font=("Arial",12),fg="black")
    #Botón mostrar
    boton_mostrar = tk.Button(ventana16, text="RESULTADOS", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionResultado)
    boton_mostrar.grid(row=5, column=0, padx=10,pady=10,sticky="w")
    
    label_M = tk.Label(ventana16, text="Es: ", font=('Arial', 12))
    label_M.grid(row=6,column=0, padx=10,pady=10,sticky="w")