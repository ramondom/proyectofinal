import tkinter as tk
import tkinter.font as tkFont
from Daccount import account

class login(tk.Toplevel):
    def __init__(self,master=None):
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
        etiqueta["font"] = ("calibri",14,"bold")
        etiqueta["fg"] = "#393d49"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta["relief"] = "flat"
        etiqueta.place(x=60,y=10,width=237,height=30)

        etiqueta_a=tk.Label(self)
        etiqueta_a["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        etiqueta_a["font"] = ("calibri",12,"bold")
        etiqueta_a["fg"] = "#333333"
        etiqueta_a["justify"] = "center"
        etiqueta_a["text"] = "usuario"
        etiqueta_a.place(x=30,y=80,width=100,height=30)

        etiqueta_b=tk.Label(self)
        etiqueta_b["bg"] = "#f2f2f2"
        
        etiqueta_b["font"] = ("calibri",12,"bold")
        etiqueta_b["fg"] = "#333333"
        etiqueta_b["justify"] = "center"
        etiqueta_b["text"] = "contraseña"
        etiqueta_b.place(x=30,y=140,width=100,height=30)

        entry_user=tk.Entry(self)
        entry_user["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_user["font"] = ft
        entry_user["fg"] = "#333333"
        entry_user["justify"] = "center"
        entry_user["text"] = "Entry"
        entry_user.place(x=150,y=80,width=190,height=30)

        entry_password=tk.Entry(self)
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = "Entry"
        entry_password.place(x=150,y=140,width=190,height=30)

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#f0f0f0"
        
        btn_inicio["font"] = ("calibri",12,"bold")
        btn_inicio["fg"] = "#000000"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "iniciar sesion"
        btn_inicio.place(x=20,y=280,width=320,height=30)
        btn_inicio["command"] = self.GButton_310_command

        GLabel_318=tk.Label(self)
        GLabel_318["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ("calibri",12,"bold")
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "No tienes cuenta? registrate aqui"
        GLabel_318.place(x=20,y=350,width=318,height=30)

        GButton_410=tk.Button(self)
        GButton_410["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_410["font"] = ("calibri",12,"bold")
        GButton_410["fg"] = "#000000"
        GButton_410["justify"] = "center"
        GButton_410["text"] = "crear cuenta"
        GButton_410.place(x=20,y=410,width=148,height=30)
        GButton_410["command"] = self.GButton_410_command

        GButton_404=tk.Button(self)
        GButton_404["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_404["font"] = ("calibri",12,"bold")
        GButton_404["fg"] = "#000000"
        GButton_404["justify"] = "center"
        GButton_404["text"] = "cancelar"
        GButton_404.place(x=190,y=410,width=149,height=30)
        GButton_404["command"] = self.GButton_404_command

        GRadio_761=tk.Checkbutton(self)
        ft = tkFont.Font(family='Times,bold',size=10)
        GRadio_761["font"] = ("calibri",12,"bold")
        GRadio_761["fg"] = "#333333"
        GRadio_761["justify"] = "center"
        GRadio_761["text"] = " Cliente"
        GRadio_761.place(x=10,y=190,width=86,height=30)
        GRadio_761["command"] = self.GRadio_761_command

        GRadio_158=tk.Checkbutton(self)
        
        GRadio_158["font"] = ("calibri",12,"bold")
        GRadio_158["fg"] = "#333333"
        GRadio_158["justify"] = "center"
        GRadio_158["text"] = " Cinemark Team"
        GRadio_158.place(x=17,y=230,width=130,height=30)
        GRadio_158["command"] = self.GRadio_158_command
        
        self.mainloop()

    def GButton_310_command(self):
        print("iniciar")


    def GButton_410_command(self):
        print("crear")
        account(self)

    def GButton_404_command(self):
        print("cancelar")
        self.destroy()


    def GRadio_761_command(self):
        print("user")


    def GRadio_158_command(self):
        print("team")
  