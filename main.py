from tkinter import *

class MyApp:
    
    """Initialiser"""
    def __init__(self, root):
        
        root.title("My app")

        """ let's define our window """
        root.geometry("500x400")

        """ We can not make it any bigger than that """
        root.maxsize(800,600)
        
        """We put the window first then parameters"""
        label = Label(root, text="Some label text")
        
        """let's make this labal appear for real"""
        label.pack()
        
""" let's create root """
root = Tk()
""" Let's create an instance of MyApp called root"""
MyApp(root)


root.mainloop()