from tkinter import *

class MyApp:
    
    """Initialiser"""
    def __init__(self, root,):
        
        root.title("My app")

        """ let's define our window """
        root.geometry("500x400")

        """ We can not make it any bigger than that """
        root.maxsize(800,600)
        
        """ We put the window first then parameters """
        label = Label(root, text="Some label text", bg="lightblue")
        
        """ let's make this label appear for real """
        label.pack()
        
        # ? Dictionary syntax which of both are better, this one ?
        # label["text"] = "New Label Text"
        # label["font"] = ("Courier")
        # ? Or this one ?
        """ configure function is quicker when ther's a lot of params to change in a row """
        label.configure(text = "New Label Text :-)", font=("Helvetica", 30))
        
        entry_text = StringVar()
        entry = Entry(root, textvariable=entry_text )
        entry.pack() # packing goes top to botton so this widget will be below the first one
        # ! We will use get & set later !
        
        label["textvariable"] = entry_text
        
# ! let's create root
root = Tk()
# ! Let's create an instance of MyApp called root
MyApp(root)


root.mainloop()