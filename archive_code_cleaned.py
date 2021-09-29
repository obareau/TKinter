from tkinter import *
import tkinter as tk
class MyApp:

    def __init__(self, root,):

        root.title("My app")
        root.geometry("500x400")
        root.maxsize(800,600)
        
        frame = Frame(root, width=200, height=100, borderwidth=2, relief="sunken")
        frame.place(x=0, y=0)
        

        self.label_text = StringVar()
        label = Label(root, text="Some label text",
                      textvariable=self.label_text, bg="lightblue")
        # label.grid(column=1, row=1)
        label.configure(text="New Label Text :-)", font=("Helvetica", 30))

        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        # ! We will use get & set later !
        # entry.grid(column=3, row=1)
    
     
        button = Button(root, text="Submit", command=self.press_button)
        # button.grid(column=1, row=2, sticky=(S, E , W))
        # button.place(x=0, y=0)
        # button.configure(width=10, height=3, font=("Helvetica", 30)) # Based on Character typographic size 
        
        self.list_items_strings = ["hey", "hi",
                                   "hello", "greetings"]  # let's make a field
        list_items = StringVar(value=self.list_items_strings)
        listbox = Listbox(root, listvariable=list_items)
        # listbox.grid(column=2, row=2)
        listbox["height"] = 3  # listbox by default contains 10 rows
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(
            listbox.curselection()))  # ! We have a tuple

    def press_button(self):
        print("Button pressed")  # Just a test
        text = self.entry_text.get()
        self.label_text.set(text)

        # ! Instance method for listbox
    def select_item(self, index):
        # ! Tuple here so we need to add a zero
        selected_item = self.list_items_strings[index[0]]
        print(selected_item) 
        # print(self.list_items_strings[index[0]])# Just a test


# ! let's create root
root = Tk()
# ! Let's create an instance of MyApp called root
MyApp(root)
root.mainloop()
