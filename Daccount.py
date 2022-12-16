import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class account(tk.Toplevel):
    def __init__(self,root,master = None):
        super().__init__(master)
        self.root = root
        self.master = master
        #setting title
        self.title("cinemark registro")
        #setting window size
        width=373
        height=505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#333333"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "nombre"
        etiqueta2.place(x=20,y=10,width=129,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#333333"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "apellido"
        etiqueta3.place(x=20,y=70,width=130,height=30)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#333333"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "DNi"
        etiqueta4.place(x=20,y=130,width=129,height=30)

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#333333"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "e-mail"
        etiqueta5.place(x=20,y=190,width=128,height=30)

        etiqueta6=tk.Label(self)
        etiqueta6["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta6["font"] = ft
        etiqueta6["fg"] = "#333333"
        etiqueta6["justify"] = "center"
        etiqueta6["text"] = "nombre de usuario"
        etiqueta6.place(x=20,y=250,width=128,height=30)

        etiqueta7=tk.Label(self)
        etiqueta7["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta7["font"] = ft
        etiqueta7["fg"] = "#333333"
        etiqueta7["justify"] = "center"
        etiqueta7["text"] = "contraseña"
        etiqueta7.place(x=20,y=310,width=129,height=30)

        etiqueta8=tk.Label(self)
        etiqueta8["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta8["font"] = ft
        etiqueta8["fg"] = "#333333"
        etiqueta8["justify"] = "center"
        etiqueta8["text"] = "conf. contraseña"
        etiqueta8.place(x=20,y=370,width=132,height=30)

        etiqueta9=tk.Label(self)
        etiqueta9["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta9["font"] = ft
        etiqueta9["fg"] = "#333333"
        etiqueta9["justify"] = "center"
        etiqueta9["text"] = "registrase como"
        etiqueta9.place(x=20,y=420,width=132,height=30)
        
        lista =["cliente","Cinemark Team"]
        roles = ttk.Combobox(self,state="readonly",values=lista,name="roleschoice")
        roles.place(x = 210,y=420)

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_inicio["font"] = ft
        btn_inicio["fg"] = "#000000"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "cancelar"
        btn_inicio.place(x=20,y=460,width=158,height=30)
        btn_inicio["command"] = self.btn_cancelar

        btn_cancelar=tk.Button(self)
        btn_cancelar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_cancelar["font"] = ft
        btn_cancelar["fg"] = "#000000"
        btn_cancelar["justify"] = "center"
        btn_cancelar["text"] = "confirmar"
        btn_cancelar.place(x=190,y=460,width=161,height=30)
        btn_cancelar["command"] = self.btn_confirmar

        entry_nombre=tk.Entry(self)
        entry_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry_nombre["font"] = ft
        entry_nombre["fg"] = "#333333"
        entry_nombre["justify"] = "center"
        entry_nombre["text"] = "entry"
        entry_nombre.place(x=170,y=10,width=181,height=30)

        entry_apellido=tk.Entry(self,name="lastname")
        entry_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry_apellido["font"] = ft
        entry_apellido["fg"] = "#333333"
        entry_apellido["justify"] = "center"
        entry_apellido["text"] = "entry"
        entry_apellido.place(x=170,y=70,width=179,height=30)

        entry_dni=tk.Entry(self)
        entry_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_dni["font"] = ft
        entry_dni["fg"] = "#333333"
        entry_dni["justify"] = "center"
        entry_dni["text"] = ""
        entry_dni.place(x=170,y=130,width=182,height=30)

        etry_correo=tk.Entry(self)
        etry_correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        etry_correo["font"] = ft
        etry_correo["fg"] = "#333333"
        etry_correo["justify"] = "center"
        etry_correo["text"] = "entry"
        etry_correo.place(x=170,y=190,width=180,height=30)

        entry_username=tk.Entry(self)
        entry_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_username["font"] = ft
        entry_username["fg"] = "#333333"
        entry_username["justify"] = "center"
        entry_username["text"] = ""
        entry_username.place(x=170,y=250,width=181,height=30)

        entry_password=tk.Entry(self,)
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = "entry"
        entry_password.place(x=170,y=310,width=179,height=30)

        entry_cpasword=tk.Entry(self")
        entry_cpasword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entry_cpasword["font"] = ft
        entry_cpasword["fg"] = "#333333"
        entry_cpasword["justify"] = "center"
        entry_cpasword["text"] = "entry"
        entry_cpasword.place(x=170,y=370,width=180,height=30)

    def btn_confirmar(self):
        print("command")


    def btn_cancelar(self):
        self.destroy()
        print("command")
