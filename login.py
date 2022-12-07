import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from user import User
from dashboard import Dashboard
import bll.usuarios as user

class Login(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.title("Login")
        #setting window size
        width=272
        height=239
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        master.geometry(alignstr)
        master.resizable(width=False, height=False)

        GLabel_109=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_109["font"] = ft
        GLabel_109["fg"] = "#333333"
        GLabel_109["justify"] = "left"
        GLabel_109["text"] = "Usuario:"
        GLabel_109.place(x=10,y=70,width=77,height=30)

        GLabel_297=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_297["font"] = ft
        GLabel_297["fg"] = "#333333"
        GLabel_297["justify"] = "left"
        GLabel_297["text"] = "Contraseña:"
        GLabel_297.place(x=20,y=110,width=70,height=25)

        GButton_594=tk.Button(self)
        GButton_594["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_594["font"] = ft
        GButton_594["fg"] = "#000000"
        GButton_594["justify"] = "left"
        GButton_594["text"] = "Aceptar"
        GButton_594.place(x=60,y=170,width=70,height=25)
        GButton_594["command"] = self.iniciar_sesion

        GButton_73=tk.Button(self)
        GButton_73["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#000000"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "Cancelar"
        GButton_73.place(x=150,y=170,width=70,height=25)
        GButton_73["command"] = self.cancelar

        GLineEdit_378=tk.Entry(self, name="txtUsuario")
        GLineEdit_378["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_378["font"] = ft
        GLineEdit_378["fg"] = "#333333"
        GLineEdit_378["justify"] = "left"
        GLineEdit_378["text"] = ""
        GLineEdit_378.place(x=90,y=70,width=144,height=30)

        GLineEdit_470=tk.Entry(self, name ="txtContrasenia", show="*")
        GLineEdit_470["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_470["font"] = ft
        GLineEdit_470["fg"] = "#333333"
        GLineEdit_470["justify"] = "left"
        GLineEdit_470["text"] = ""
        GLineEdit_470.place(x=90,y=110,width=144,height=30)

        GButton_493=tk.Button(self)
        GButton_493["bg"] = "#e9e9ed"
        GButton_493["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=9, underline=True, weight='bold')
        GButton_493["font"] = ft
        GButton_493["fg"] = "#000000"
        GButton_493["justify"] = "center"
        GButton_493["text"] = "Crear Cuenta"
        GButton_493.place(x=130,y=20,width=102,height=30)
        GButton_493["command"] = self.crear_user

    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtContrasenia = self.nametowidget("txtContrasenia")
            contrasenia = txtContrasenia.get()

            if usuario != "":
                if user.validar(usuario, contrasenia):
                    Dashboard(self.master)
                    self.destroy()
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cancelar(self):
        self.destroy()

    def crear_user(self):
        User(self.master)

