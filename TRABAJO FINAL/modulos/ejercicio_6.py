#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_6():
    
    def funcionMostrar():
        sexo = txtsexo.get()
        edad =  float(txtedad.get())
        if sexo == "masculino" and edad >= 18 :
            label_S.config(text=f"Hola {txtnombre.get()}", font=("arial",12,"bold"))
        if sexo == "masculino" and edad <= 17 :
            label_S.config(text=f"Hola no eres mayor de edad", font=("arial",12,"bold"))
        else:
            label_S.config(text=f"Hola chica", font=("arial",12,"bold"))
    ventana8 = tk.Tk()
    ventana8.title("EJERCICIO 6")
    ventana8.geometry("400x400")
    ventana8.resizable(False,False)
    ventana8.iconbitmap("icons/favicon.ico")
    #Titulo
    label_titulo = tk.Label(ventana8,text="NOMBRE&EDAD&SEXO", font=("Arial",15,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #Nombre
    label_nombre = tk.Label(ventana8,text="Ingrese su nombre", font=("Arial",10,"bold"))
    label_nombre.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #Nombre escritura
    txtnombre = tk.Entry(ventana8,font=("Arial",10,"bold"))
    txtnombre.grid(row=2,column=0,columnspan=1,padx=10,sticky="w")
    txtnombre.config(bg="#fff",font=("Arial",12),fg="black")
    #Edad
    label_edad = tk.Label(ventana8,text="Edad", font=("Arial",10,"bold"))
    label_edad.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #Edad escritura
    txtedad= tk.Entry(ventana8,font=("Arial",10,"bold"))
    txtedad.grid(row=4,column=0,columnspan=1,padx=10,sticky="w")
    txtedad.config(bg="#fff",font=("Arial",12),fg="black")
    #Sexo
    label_sexo = tk.Label(ventana8,text="Ingrese su sexo", font=("Arial",10,"bold"))
    label_sexo.grid(row=5,column=0,padx=10,pady=10,sticky="w")
    #Sexo escritura
    txtsexo = tk.Entry(ventana8,font=("Arial",10,"bold"))
    txtsexo.grid(row=6,column=0,columnspan=1,padx=10,sticky="w")
    txtsexo.config(bg="#fff",font=("Arial",12),fg="black")
    #Botón
    boton = tk.Button(ventana8, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionMostrar)
    boton.grid(row=7, column=0, padx=10,pady=10,sticky="w")
    
    label_S = tk.Label(ventana8, text="Es: ", font=('Arial', 12))
    label_S.grid(row=8,column=0, padx=10,pady=10,sticky="w")