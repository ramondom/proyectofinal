from tkinter import *
import bll.usuarios as user
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgbox
import string

class account(Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("cinemar registro")
        #setting window size
        width=373
        height=505
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta1= Label(self)
        etiqueta1["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta1["font"] = ft
        etiqueta1["fg"] = "#333333"
        etiqueta1["justify"] = "center"
        etiqueta1["text"] = "registro usuario"
        etiqueta1.place(x=60,y=0,width=242,height=30)

        etiqueta2= Label(self)
        etiqueta2["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#333333"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "nombre"
        etiqueta2.place(x=20,y=40,width=129,height=30)

        etiqueta3= Label(self)
        etiqueta3["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#333333"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "apellido"
        etiqueta3.place(x=20,y=100,width=130,height=30)

        etiqueta4= Label(self)
        etiqueta4["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#333333"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "DNi"
        etiqueta4.place(x=20,y=160,width=129,height=30)

        etiqueta5= Label(self)
        etiqueta5["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#333333"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "e-mail"
        etiqueta5.place(x=20,y=220,width=128,height=30)

        etiqueta6= Label(self)
        etiqueta6["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta6["font"] = ft
        etiqueta6["fg"] = "#333333"
        etiqueta6["justify"] = "center"
        etiqueta6["text"] = "nombre de usuario"
        etiqueta6.place(x=20,y=280,width=128,height=30)

        etiqueta7= Label(self)
        etiqueta7["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta7["font"] = ft
        etiqueta7["fg"] = "#333333"
        etiqueta7["justify"] = "center"
        etiqueta7["text"] = "contraseña"
        etiqueta7.place(x=20,y=340,width=129,height=30)

        etiqueta8= Label(self)
        etiqueta8["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta8["font"] = ft
        etiqueta8["fg"] = "#333333"
        etiqueta8["justify"] = "center"
        etiqueta8["text"] = "conf. contraseña"
        etiqueta8.place(x=20,y=400,width=132,height=30)

        btn_inicio= Button(self)
        btn_inicio["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_inicio["font"] = ft
        btn_inicio["fg"] = "#000000"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "cancelar"
        btn_inicio.place(x=20,y=460,width=158,height=30)
        btn_inicio["command"] = self.btn_cancelar

        btn_cancelar= Button(self)
        btn_cancelar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_cancelar["font"] = ft
        btn_cancelar["fg"] = "#000000"
        btn_cancelar["justify"] = "center"
        btn_cancelar["text"] = "confirmar"
        btn_cancelar.place(x=190,y=460,width=161,height=30)
        btn_cancelar["command"] = self.btn_confirmar

        entry_nombre= Entry(self,name="name")
        entry_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_nombre["font"] = ft
        entry_nombre["fg"] = "#333333"
        entry_nombre["justify"] = "center"
        entry_nombre["text"] = ""
        entry_nombre.place(x=170,y=40,width=181,height=30)

        entry_apellido= Entry(self,name="lastname")
        entry_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_apellido["font"] = ft
        entry_apellido["fg"] = "#333333"
        entry_apellido["justify"] = "center"
        entry_apellido["text"] = ""
        entry_apellido.place(x=170,y=100,width=179,height=30)

        entry_dni= Entry(self,name="dni")
        entry_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_dni["font"] = ft
        entry_dni["fg"] = "#333333"
        entry_dni["justify"] = "center"
        entry_dni["text"] = ""
        entry_dni.place(x=170,y=160,width=182,height=30)

        etry_correo= Entry(self,name="email")
        etry_correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        etry_correo["font"] = ft
        etry_correo["fg"] = "#333333"
        etry_correo["justify"] = "center"
        etry_correo["text"] = ""
        etry_correo.place(x=170,y=220,width=180,height=30)

        entry_username= Entry(self,name="username")
        entry_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_username["font"] = ft
        entry_username["fg"] = "#333333"
        entry_username["justify"] = "center"
        entry_username["text"] = ""
        entry_username.place(x=170,y=280,width=181,height=30)

        entry_password= Entry(self,name="password",show="*")
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = ""
        entry_password.place(x=170,y=340,width=179,height=30)

        entry_cpasword= Entry(self,name="password2",show="*")
        entry_cpasword["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_cpasword["font"] = ft
        entry_cpasword["fg"] = "#333333"
        entry_cpasword["justify"] = "center"
        entry_cpasword["text"] = ""
        entry_cpasword.place(x=170,y=400,width=180,height=30)

    def get_value(self, name):
        return self.nametowidget(name).get()

    def btn_confirmar(self):
        nombre = self.get_value("name")
        apellido = self.get_value("lastname")
        dni = self.get_value("dni")
        user = self.get_value("username")
        email = self.get_value("email")
        password=self.get_value("password")
        password_Conf = self.get_value("password2")

        if nombre == None or apellido == "" or dni == "" or user == "" or email == "" or password == "" or password_Conf == "":
            tkMsgbox.showwarning(self.title(),"todos los campos deben estar completos!")
        else:
            if password.isalnum() and len(password) >= 8:
                if password == password_Conf:
                    tkMsgbox.showinfo(self.title(),"registro existoso")
                else:
                    tkMsgbox.showerror(self.title(),"las contraseñas no coinciden")
            else:
                tkMsgbox.showwarning(self.title(),"la contraseña debe tenr al menos un numero y no ser menor a 8 caracteres")
        print("confirmar")


    def btn_cancelar(self):
        self.destroy()
        print("cancelar")
