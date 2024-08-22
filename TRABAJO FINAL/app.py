#Importamos el TKINTER
import tkinter as tk
#Importamos los messageBox
from tkinter import messagebox
#Importamos el modulo del archivo principal y usar todo*
from modulos.principal import *

#Creamos una funcion para mostrar mensajes
def ingreso():
    Usuario = "Luis"
    Contraseña = "Diaz"
    user = txtusuario.get()
    password = txtcontraseña.get()
    if Usuario == user and Contraseña == password:
        messagebox.showinfo(title="Mensaje", message="BIENVENIDO :)")
        ventana.destroy()
        abrirVentanaPrincipal()
    else:
        messagebox.showerror(title="Mensaje", message="DATOS INCORRECTOS, INTENTE OTRA VEZ")
    
    
#Inicializamos la clase TK()
ventana = tk.Tk() 
#Menciono el nombre de la ventana
ventana.title("SENATI")
#Icono en la ventana
ventana.iconbitmap("icons/favicon.ico")
#Tamaño de la ventana
ventana.geometry("350x350")
#Color del fondo de la ventana
ventana.config(bg="#ffffff")
#El usuario no permite modificar la ventana
ventana.resizable(False,False)
#Inicio de sesión
label_login = tk.Label(ventana,text="Iniciar Sesión", font=("Arial",20,"bold"))
label_login.grid(row=0,column=0,padx=60,pady=10)
label_login.config(bg="#ffffff")
#Usuario
label_usuario = tk.Label(ventana,text="Usuario", font=("Arial",15,"bold"))
label_usuario.grid(row=1,column=0,padx=10,pady=10,sticky="w")
label_usuario.config(bg="#ffffff")
#Usuario escritura
txtusuario = tk.Entry(ventana,font=("Arial",12,"bold"))
txtusuario.grid(row=2,column=0,padx=10,sticky="w")
txtusuario.config(bg="#fff",font=("Arial",12),fg="black")
#Contraseña
label_contraseña = tk.Label(ventana,text="Contraseña", font=("Arial",15,"bold"))
label_contraseña.grid(row=3,column=0,padx=10,pady=10,sticky="w")
label_contraseña.config(bg="#ffffff")
#Contraseña escritura
txtcontraseña = tk.Entry(ventana,font=("Arial",12,"bold"))
txtcontraseña.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtcontraseña.config(bg="#fff",font=("Arial",12),fg="black",show="*")

#AGREGANDO BOTONES
boton3 = tk.Button(ventana, text="INGRESAR", width=12,height=1,fg="white", bg="blue", font=("Arial",12, "bold"), command=ingreso)
boton3.grid(row=5,column=0,padx=10,pady=10,sticky="w",)



#Mantener la ventana abierta
ventana.mainloop()