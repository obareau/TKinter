from tkinter import *
import tkinter as tk

class MyApp:
    
    """Initialiser"""
    def __init__(self, root,):
        
        root.title("My app")

        # """ let's define our window """
        # root.geometry("500x400")

        # """ We can not make it any bigger than that """
        # root.maxsize(800,600)
        
        self.label_text = StringVar()
        
        """ We put the window first then parameters """
        label = Label(root, text="Some label text", textvariable=self.label_text, bg="lightblue")
        
        """ let's make this label appear for real """
        label.pack(side=tk.LEFT, padx=10, pady=5, ) 
        """Widgets are aligned left to right with a padding between it 
        keep in mind all widhets are glued together"""
        
        # ? Dictionary syntax which of both are better, this one ?
        # label["text"] = "New Label Text"
        # label["font"] = ("Courier")
        # ? Or this one ?
        """ configure function is quicker when ther's a lot of params to change in a row """
        label.configure(text = "New Label Text :-)", font=("Helvetica", 30))
        
        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text )
        entry.pack(side=tk.LEFT) # packing goes top to botton so this widget will be below the first one
        # ! We will use get & set later !
        
        # label["textvariable"] = entry_text
        button = Button(root,text="Submit", command=self.press_button)
        button.pack(side=tk.LEFT)
        
        self.list_items_strings = ["hey", "hi", "hello", "greetings"] # let's make a field
        list_items = StringVar(value=self.list_items_strings)
        listbox = Listbox(root, listvariable=list_items)
        listbox.pack(side=tk.LEFT, padx=40, pady=20, )
        listbox["height"] = 3 #listbox by default contains 10 rows
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection())) # ! We have a tuple
        
    def press_button(self):
        print("Button pressed") # Just a test 
        text = self.entry_text.get()
        self.label_text.set(text)
        
        # ! Instance method for listbox
    def select_item(self, index):
        selected_item =  self.list_items_strings[index[0]] # ! Tuple here so we need to add a zero
        print(selected_item) # Just a test
        
        
        
        
        
# ! let's create root
root = Tk()
# ! Let's create an instance of MyApp called root
MyApp(root)


root.mainloop()