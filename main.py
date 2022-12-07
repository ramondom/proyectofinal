import tkinter as tk
import tkinter.font as tkFont
from login import Login
from dal.db import Db

class App:
    def __init__(self, root, title):
        self.root = root
        root.title(title)
        #setting window size
        width=379
        height=147
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_850=tk.Button(root)
        GButton_850["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_850["font"] = ft
        GButton_850["fg"] = "#000000"
        GButton_850["justify"] = "left"
        GButton_850["text"] = "Abrir Cine"
        GButton_850.place(x=120,y=50,width=130,height=30)
        GButton_850["command"] = self.abrir_login

    def abrir_login(self):
        Login(self.root)

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    project = "cinemark"
    root = tk.Tk()
    root.iconbitmap(default=f"{project}.ico")
    app = App(root, project.capitalize())
    root.mainloop()


