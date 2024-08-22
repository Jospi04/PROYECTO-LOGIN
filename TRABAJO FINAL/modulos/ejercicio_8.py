#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirventanaejercicio_8():
    
    def funcionBuscar():
        letra = txtletra.get()
        if letra == "A" or letra == "a":
            messagebox.showinfo(title="MENSAJE", message="Es la vocal a")
        elif letra == "E" or letra == "e":
            messagebox.showinfo(title="MENSAJE", message="Es la vocal e")
        elif letra == "I" or letra == "i":
            messagebox.showinfo(title="MENSAJE", message="Es la vocal i")
        elif letra == "O" or letra == "o":
            messagebox.showinfo(title="MENSAJE", message="Es la vocal o")
        elif letra == "U" or letra == "u":
            messagebox.showinfo(title="MENSAJE", message="Es la vocal u")
        else:
            messagebox.showinfo(title="MENSAJE", message="Es una consonante")
        
    ventana10 = tk.Tk()
    ventana10.title("EJERCICIO 8")
    ventana10.geometry("330x300")
    ventana10.resizable(False,False)
    ventana10.iconbitmap("icons/favicon.ico")
    
    #Titulo del ejercicio
    label_titulo = tk.Label(ventana10,text="LETRAS", font=("Arial",12,"bold"))
    label_titulo.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="w")
    #LETRA
    label_letra = tk.Label(ventana10,text="Escriba una letra", font=("Arial",8,"bold"))
    label_letra.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    #LETRA escritura
    txtletra = tk.Entry(ventana10,font=("Arial",8,"bold"))
    txtletra.grid(row=2,column=0,padx=10,sticky="w")
    txtletra.config(bg="#fff",font=("Arial",12),fg="black")
    #boon
    boton = tk.Button(ventana10, text="MOSTRAR", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionBuscar)
    boton.grid(row=11, column=0, padx=10,pady=10,sticky="w")
    