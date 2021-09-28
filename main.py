from tkinter import *

class MyApp:
    
    """Initialiser"""
    def __init__(self, root,):
        
        root.title("My app")

        """ let's define our window """
        root.geometry("500x400")

        """ We can not make it any bigger than that """
        root.maxsize(800,600)
        
        self.label_text = StringVar()
        
        """ We put the window first then parameters """
        label = Label(root, text="Some label text", textvariable=self.label_text, bg="lightblue")
        
        """ let's make this label appear for real """
        label.pack()
        
        # ? Dictionary syntax which of both are better, this one ?
        # label["text"] = "New Label Text"
        # label["font"] = ("Courier")
        # ? Or this one ?
        """ configure function is quicker when ther's a lot of params to change in a row """
        label.configure(text = "New Label Text :-)", font=("Helvetica", 30))
        
        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text )
        entry.pack() # packing goes top to botton so this widget will be below the first one
        # ! We will use get & set later !
        
        # label["textvariable"] = entry_text
        button = Button(root,text="Submit", command=self.press_button)
        button.pack()
    def press_button(self):
        print("Button pressed") # Just a test 
        text = self.entry_text.get()
        self.label_text.set(text)
        
        
        
# ! let's create root
root = Tk()
# ! Let's create an instance of MyApp called root
MyApp(root)


root.mainloop()