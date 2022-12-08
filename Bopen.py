import tkinter as tk
import tkinter.font as tkFont
from Clogin import login
from Daccount import account

class App:
    def __init__(self,ventana,root):
        self.root = root
        #setting title
        ventana.title("Cinemark")
        #setting window size
        width=483
        height=156
        screenwidth = ventana.winfo_screenwidth()
        screenheight = ventana.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        ventana.geometry(alignstr)
        ventana.resizable(width=False, height=False)

        etiqueta=tk.Label(ventana)
        etiqueta["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=12)
        etiqueta["font"] = ("calibri",14,"bold")
        etiqueta["fg"] = "#393d49"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta["relief"] = "flat"
        etiqueta.place(x=120,y=10,width=237,height=30)

        btn_open=tk.Button(ventana)
        btn_open["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        btn_open["font"] = ("calibri",12,"bold")
        btn_open["fg"] = "#000000"
        btn_open["justify"] = "center"
        btn_open["text"] = "iniciar"
        btn_open.place(x=70,y=80,width=157,height=30)
        btn_open["command"] = self.open_app

        btn_close=tk.Button(ventana)
        btn_close["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='Times',size=10)
        btn_close["font"] = ("calibri",12,"bold")
        btn_close["fg"] = "#000000"
        btn_close["justify"] = "center"
        btn_close["text"] = "cancelar"
        btn_close.place(x=250,y=80,width=152,height=30)
        btn_close["command"] = self.close_app

    def open_app(self):
        print("open")
        login(self.root)


    def close_app(self):
        print("close")
        ventana.destroy()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana,root=ventana)
    ventana.iconbitmap(default="zcinemark.ico")

    ventana.mainloop()