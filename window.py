from tkinter import *
from UMLMaker import show_table

def set_parameters():
    """Receives user input for the necessary values of the diagram and assigns them to variables"""
    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("500x320+0+0")

    Label(root, text="Enter the coding language of the file", font=("time new roman",10)).place(x=20,y=100)
    Label(root, text="Enter the file", font=("time new roman",10)).place(x=20,y=120)

    lang = Entry(root)
    file = Entry(root) 

    def show_uml(lang, file):
        show_table(lang, file)

    lang.place(x=300,y=100)
    file.place(x=300,y=120)
     
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=270)
    Button(root, text='Submit',width=5, command=show_uml(lang, file)).place(x=100,y=270)

    mainloop()

set_parameters()
