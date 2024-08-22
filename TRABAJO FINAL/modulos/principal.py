#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from modulos.ejercicio_1 import *
from modulos.ejercicio_2 import *
from modulos.ejercicio_3 import *
from modulos.ejercicio_4 import *
from modulos.ejercicio_5 import *
from modulos.ejercicio_6 import *
from modulos.ejercicio_7 import *
from modulos.ejercicio_8 import *
from modulos.ejercicio_9 import *
from modulos.ejercicio_10 import *
from modulos.ejercicio_11 import *
from modulos.ejercicio_12 import *
from modulos.ejercicio_13 import *
from modulos.ejercicio_14 import *
from modulos.ejercicio_15 import *

def abrirVentanaPrincipal():
    
    def functionejercicio01():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 1")
        abrirventanaejercicio_1()
    def functionejercicio02():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 2")
        abrirventanaejercicio_2()
    def functionejercicio03():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 3")
        abrirventanaejercicio_3()
    def functionejercicio04():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 4")
        abrirventanaejercicio_4()
    def functionejercicio05():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 5")
        abrirventanaejercicio_5()
    def functionejercicio06():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 6")
        abrirventanaejercicio_6()
    def functionejercicio07():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 7")
        abrirventanaejercicio_7()
    def functionejercicio08():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 8")
        abrirventanaejercicio_8()
    def functionejercicio09():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 9")
        abrirventanaejercicio_9()
    def functionejercicio10():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 10")
        abrirventanaejercicio_10()  
    def functionejercicio11():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 11")
        abrirventanaejercicio_11()    
    def functionejercicio12():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 12")
        abrirventanaejercicio_12()    
    def functionejercicio13():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 13")
        abrirventanaejercicio_13()    
    def functionejercicio14():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 14")
        abrirventanaejercicio_14()
    def functionejercicio15():
        messagebox.showinfo("Mensaje", "Yendo al ejercicio 15")
        abrirventanaejercicio_15()
            
          
    ventana2 = tk.Tk()
    ventana2.title("EJERCICIOS")
    ventana2.geometry("515x320")
    ventana2.iconbitmap("icons/favicon.ico")
    ventana2.resizable(False,False)
    ventana2.config(bg="#ffffff")
    

    ##BOTON DE EJERCICIO 1
    boton_ejercicio1 = tk.Button(ventana2, text="EJERCICIO 1", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio01)
    boton_ejercicio1.grid(row=0, column=0,columnspan=1,padx=10, pady=10)

    ##BOTON DE EJERCICIO 2
    boton_ejercicio2 = tk.Button(ventana2, text="EJERCICIO 2", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio02)
    boton_ejercicio2.grid(row=0, column=1,columnspan=1,padx=10, pady=10)

    ##BOTON DE EJERCICIO 3
    boton_ejercicio3 = tk.Button(ventana2, text="EJERCICIO 3", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio03)
    boton_ejercicio3.grid(row=0, column=2,columnspan=1,padx=10, pady=10)

    ##BOTON DE EJERCICIO 4
    boton_ejercicio4 = tk.Button(ventana2, text="EJERCICIO 4", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio04)
    boton_ejercicio4.grid(row=1, column=0,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 5
    boton_ejercicio5 = tk.Button(ventana2, text="EJERCICIO 5", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio05)
    boton_ejercicio5.grid(row=1, column=1,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 6
    boton_ejercicio6 = tk.Button(ventana2, text="EJERCICIO 6", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio06)
    boton_ejercicio6.grid(row=1, column=2,columnspan=2,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 7
    boton_ejercicio8 = tk.Button(ventana2,text="EJERCICIO 7", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio07)
    boton_ejercicio8.grid(row=2, column=0,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 8
    boton_ejercicio8 = tk.Button(ventana2, text="EJERCICIO 8", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio08)
    boton_ejercicio8.grid(row=2, column=1,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 9
    boton_ejercicio9 = tk.Button(ventana2, text="EJERCICIO 9", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio09)
    boton_ejercicio9.grid(row=2, column=2,columnspan=2,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 10
    boton_ejercicio10 = tk.Button(ventana2, text="EJERCICIO 10", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio10)
    boton_ejercicio10.grid(row=3, column=0,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 11
    boton_ejercicio11 = tk.Button(ventana2, text="EJERCICIO 11", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio11)
    boton_ejercicio11.grid(row=3, column=1,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 12
    boton_ejercicio12 = tk.Button(ventana2, text="EJERCICIO 12", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio12)
    boton_ejercicio12.grid(row=3, column=2,columnspan=2,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 13
    boton_ejercicio13 = tk.Button(ventana2, text="EJERCICIO 13", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio13)
    boton_ejercicio13.grid(row=4, column=0,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 14
    boton_ejercicio14 = tk.Button(ventana2, text="EJERCICIO 14", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio14)
    boton_ejercicio14.grid(row=4, column=1,columnspan=1,padx=10, pady=10)
    
    ##BOTON DE EJERCICIO 15
    boton_ejercicio15 = tk.Button(ventana2, text="EJERCICIO 15", fg="white",bg="blue" , font=("Arial", 12, "bold"), command=functionejercicio15)
    boton_ejercicio15.grid(row=4, column=2,columnspan=2,padx=10, pady=10)
    
    #poner siempre al ultimo, ya que esto permitira que este activo la ventana
    ventana2.mainloop() 
    

#abrirVentanaPrincipal()