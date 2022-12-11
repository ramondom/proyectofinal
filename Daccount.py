from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

class account(Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("Cinemark login")
        #setting window size
        width=373
        height=505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta=tk.Label(self)
        etiqueta["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta["font"] = ("calibri",12,"bold")
        etiqueta["fg"] = "#333333"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta.place(x=40,y=10,width=282,height=30)

        etiqueta1=tk.Label(self)
        etiqueta1["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta1["font"] =("calibri",12,"bold")
        etiqueta1["fg"] = "#393d49"
        etiqueta1["justify"] = "center"
        etiqueta1["text"] = "nombre"
        etiqueta1.place(x=20,y=80,width=135,height=30)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta2["font"] = ("calibri",12,"bold")
        etiqueta2["fg"] = "#333333"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "apellido"
        etiqueta2.place(x=20,y=140,width=131,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta3["font"] = ("calibri",12,"bold")
        etiqueta3["fg"] = "#333333"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "DNI"
        etiqueta3.place(x=20,y=200,width=130,height=30)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta4["font"] = ("calibri",12,"bold")
        etiqueta4["fg"] = "#333333"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "e-mail"
        etiqueta4.place(x=20,y=260,width=129,height=30)

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta5["font"] = ("calibri",12,"bold")
        etiqueta5["fg"] = "#333333"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "usuario"
        etiqueta5.place(x=20,y=320,width=131,height=30)

        etiqueta6=tk.Label(self)
        etiqueta6["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta6["font"] = ("calibri",12,"bold")
        etiqueta6["fg"] = "#333333"
        etiqueta6["justify"] = "center"
        etiqueta6["text"] = "contraeña"
        etiqueta6.place(x=20,y=380,width=131,height=30)

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_inicio["font"] = ("calibri",12,"bold")
        btn_inicio["fg"] = "#000000"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "iniciar secion"
        btn_inicio.place(x=30,y=440,width=141,height=30)
        btn_inicio["command"] = self.inicio

        btn_cancelar=tk.Button(self)
        btn_cancelar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_cancelar["font"] = ("calibri",12,"bold")
        btn_cancelar["fg"] = "#000000"
        btn_cancelar["justify"] = "center"
        btn_cancelar["text"] = "cancelar"
        btn_cancelar.place(x=200,y=440,width=142,height=30)
        btn_cancelar["command"] = self.cancelar

        entry_name=tk.Entry(self)
        entry_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_name["font"] = ft
        entry_name["fg"] = "#333333"
        entry_name["justify"] = "center"
        entry_name["text"] = "Entry"
        entry_name.place(x=170,y=80,width=180,height=30)

        entry_lastname=tk.Entry(self)
        entry_lastname["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_lastname["font"] = ft
        entry_lastname["fg"] = "#333333"
        entry_lastname["justify"] = "center"
        entry_lastname["text"] = "Entry"
        entry_lastname.place(x=170,y=140,width=182,height=30)

        entry_id=tk.Entry(self)
        entry_id["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_id["font"] = ft
        entry_id["fg"] = "#333333"
        entry_id["justify"] = "center"
        entry_id["text"] = "Entry"
        entry_id.place(x=170,y=200,width=181,height=30)

        entry_mail=tk.Entry(self)
        ft = tkFont.Font(family='calibri',size=12)
        entry_mail["font"] = ft
        entry_mail["fg"] = "#333333"
        entry_mail["justify"] = "center"
        entry_mail["text"] = "Entry"
        entry_mail.place(x=170,y=260,width=181,height=30)

        entry_user=tk.Entry(self)
        entry_user["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_user["font"] = ft
        entry_user["fg"] = "#333333"
        entry_user["justify"] = "center"
        entry_user["text"] = "Entry"
        entry_user.place(x=170,y=320,width=181,height=30)

        entry_password=tk.Entry(self)
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=10)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = "Entry"
        entry_password.place(x=170,y=380,width=182,height=30)

        self.mainloop()

    def inicio(self):
        print("inicio")


    def cancelar(self):
        print("command")
        self.destroy()