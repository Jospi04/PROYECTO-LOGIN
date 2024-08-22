#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_13():
    
    ventana15 = tk.Tk()
    ventana15.title("EJERCICIO 13")
    ventana15.geometry("415x410")
    ventana15.resizable(False,False)
    ventana15.iconbitmap("icons/favicon.ico")
    
    def funcionPromedio():
        nota1 = int(txtnota1.get())
        nota2 = int(txtnota2.get())
        nota3 = int(txtnota3.get())
        resultado = (nota1+nota2+nota3)/3
        if resultado <= 10:
            labelpromedio.config(text=f"EL PROMEDIO ES: {resultado}",font=("arial",12,"bold"))
            labelcomentario.config(text=f"MALO", font=("arial",12,"bold"))
        elif resultado >= 11 and resultado <=13:
            labelpromedio.config(text=f"EL PROMEDIO ES: {resultado}",font=("arial",12,"bold"))
            labelcomentario.config(text=f"REGULAR", font=("arial",12,"bold"))
        elif resultado >=14 and resultado <=17:
            labelpromedio.config(text=f"EL PROMEDIO ES: {resultado}",font=("arial",12,"bold"))
            labelcomentario.config(text=f"BUENO", font=("arial",12,"bold"))
        elif resultado >=18 and resultado <=20:
            labelpromedio.config(text=f"EL PROMEDIO ES: {resultado}",font=("arial",12,"bold"))
            labelcomentario.config(text=f"EXCELENTE", font=("arial",12,"bold"))
            
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana15,text="Ingrese tres notas", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    
    #NOTA 1
    label_nota1 = tk.Label(ventana15,text="NOTA UNO", font=("Arial",8,"bold"))
    label_nota1.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #NOTA 1 escritura
    txtnota1 = tk.Entry(ventana15,font=("Arial",8,"bold"))
    txtnota1.grid(row=2,column=0,padx=10,sticky="w")
    txtnota1.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 2
    label_nota2 = tk.Label(ventana15,text="NOTA DOS", font=("Arial",8,"bold"))
    label_nota2.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #NOTA 2 escritura
    txtnota2 = tk.Entry(ventana15,font=("Arial",8,"bold"))
    txtnota2.grid(row=4,column=0,padx=10,sticky="w")
    txtnota2.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 3
    label_nota3 = tk.Label(ventana15,text="NOTA TRES", font=("Arial",8,"bold"))
    label_nota3.grid(row=5,column=0,padx=10,pady=10,sticky="w")
    #NOTA 3 escritura
    txtnota3 = tk.Entry(ventana15,font=("Arial",8,"bold"))
    txtnota3.grid(row=6,column=0,padx=10,sticky="w")
    txtnota3.config(bg="#fff",font=("Arial",12),fg="black")
    
    #botón promedio
    boton_promedio = tk.Button(ventana15, text="PROMEDIAR",fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionPromedio)
    boton_promedio.grid(row=7, column=0, padx=10,pady=10,sticky="w")
    
    labelpromedio = tk.Label(ventana15, text="Es: ", font=('Arial', 12))
    labelpromedio.grid(row=8,column=0, padx=10,pady=10,sticky="w")
    
    labelcomentario = tk.Label(ventana15, text="Es: ", font=('Arial', 12))
    labelcomentario.grid(row=9,column=0, padx=10,pady=10,sticky="w")