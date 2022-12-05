import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=379
        height=147
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_404=tk.Button(root)
        GButton_404["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_404["font"] = ft
        GButton_404["fg"] = "#000000"
        GButton_404["justify"] = "center"
        GButton_404["text"] = "Abrir Cine"
        GButton_404.place(x=80,y=50,width=210,height=34)
        GButton_404["command"] = self.GButton_404_command

    def GButton_404_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
