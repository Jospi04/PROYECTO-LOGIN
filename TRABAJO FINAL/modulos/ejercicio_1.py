#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_1():
    
    def funcionPromedio():
        nota1 = int(txtnota1.get())
        nota2 = int(txtnota2.get())
        nota3 = int(txtnota3.get())
        resultado = (nota1+nota2+nota3)/3
        labelpromedio.config(text=f"EL PROMEDIO ES: {resultado}",font=("arial",12,"bold"))
        if resultado <= 10:
            messagebox.showinfo(title="MENSAJE", message="DESAPROBADO")
        else:
            messagebox.showinfo(title="MENSAJE", message="APROBADO")
        
        
        
    ventana3 = tk.Tk()
    ventana3.title("EJERCICIO 1")
    ventana3.geometry("400x400")
    ventana3.resizable(False,False)
    ventana3.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana3,text="Ingrese tres notas", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    
    #NOTA 1
    label_nota1 = tk.Label(ventana3,text="NOTA UNO", font=("Arial",8,"bold"))
    label_nota1.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #NOTA 1 escritura
    txtnota1 = tk.Entry(ventana3,font=("Arial",8,"bold"))
    txtnota1.grid(row=2,column=0,padx=10,sticky="w")
    txtnota1.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 2
    label_nota2 = tk.Label(ventana3,text="NOTA DOS", font=("Arial",8,"bold"))
    label_nota2.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    #NOTA 2 escritura
    txtnota2 = tk.Entry(ventana3,font=("Arial",8,"bold"))
    txtnota2.grid(row=4,column=0,padx=10,sticky="w")
    txtnota2.config(bg="#fff",font=("Arial",12),fg="black")
    
    #NOTA 3
    label_nota3 = tk.Label(ventana3,text="NOTA TRES", font=("Arial",8,"bold"))
    label_nota3.grid(row=5,column=0,padx=10,pady=10,sticky="w")
    #NOTA 3 escritura
    txtnota3 = tk.Entry(ventana3,font=("Arial",8,"bold"))
    txtnota3.grid(row=6,column=0,padx=10,sticky="w")
    txtnota3.config(bg="#fff",font=("Arial",12),fg="black")
    
    #botón promedio
    boton_promedio = tk.Button(ventana3, text="PROMEDIAR",fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionPromedio)
    boton_promedio.grid(row=7, column=0, padx=10,pady=10,sticky="w")
    
    labelpromedio = tk.Label(ventana3, text="Es: ", font=('Arial', 12))
    labelpromedio.grid(row=8,column=0, padx=10,pady=10,sticky="w")