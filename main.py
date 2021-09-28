from tkinter import *

class MyApp:
    
    def __init__(self, root):
        root.title("My app")

        """ let's define our window """
        root.geometry("500x400")

        """ We can not make it any bigger thant that """
        root.maxsize(800,600)

root = Tk()
""" Let's create an instance of MyApp called root"""
MyApp(root)


root.mainloop()