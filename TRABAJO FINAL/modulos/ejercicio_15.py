#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from modulos.inicio_final import *


def abrirventanaejercicio_15():
    def ingreso():
        if txt_usuario.get() == "luis" and txtcontraseña.get() == "pepe":
            messagebox.showinfo(title="Mensaje", message="BIENVENIDO :)")

    
    ventana17 = tk.Tk()
    ventana17.title("EJERCICIO 15")
    ventana17.geometry("400x400")
    ventana17.resizable(False,False)
    ventana17.iconbitmap("icons/favicon.ico")
    ventana17.config(bg="#ffffff")
    
    label_login = tk.Label(ventana17,text="Iniciar Sesión", font=("Arial",20,"bold"))
    label_login.grid(row=0,column=0,padx=60,pady=10)
    label_login.config(bg="#ffffff")
    
    label_usuario = tk.Label(ventana17,text="Usuario", font=("Arial",15,"bold"))
    label_usuario.grid(row=1,column=0,padx=10,pady=10,sticky="w")
    label_usuario.config(bg="#ffffff")
    
    txt_usuario = tk.Entry(ventana17, font=("Arial",15,"bold"))
    txt_usuario.grid(row=2,column=0,padx=10,pady=10,sticky="w")
    txt_usuario.config(bg="#ffffff")
    
    #Contraseña
    label_contraseña = tk.Label(ventana17,text="Contraseña", font=("Arial",15,"bold"))
    label_contraseña.grid(row=3,column=0,padx=10,pady=10,sticky="w")
    label_contraseña.config(bg="#ffffff")
    #Contraseña escritura
    txtcontraseña = tk.Entry(ventana17,font=("Arial",12,"bold"))
    txtcontraseña.grid(row=4,column=0,padx=10,pady=10,sticky="w")
    txtcontraseña.config(bg="#fff",font=("Arial",12),fg="black",show="*")
    
    boton3 = tk.Button(ventana17, text="INGRESAR", width=12,height=1,fg="white", bg="blue", font=("Arial",12, "bold"), command=ingreso)
    boton3.grid(row=5,column=0,padx=10,pady=10,sticky="w",)
    