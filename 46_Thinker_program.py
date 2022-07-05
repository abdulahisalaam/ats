from tkinter import * 
from tkinter import ttk
root = Tk()
root.configure(bg="#030E4F")
root.geometry("700x350")
e = Entry(root,width=50, borderwidth=5, text="Enter Your name: ")
e.pack()
def clickedme():
    myLabell = Label(root, text=e.get(), bg="#030E4F", fg="#F49F1C")
    myLabell.pack()
# my_label1 = Label(root, text = "Hello World").grid(row=0,column=1)
# my_label2 = Label(root, text = "My name is Abdullah").grid(row=1,column=1)
# my_label1.grid(row=0,column=1)
# my_label2.grid(row=1,column=1)
my_button = Button(root, text="Click Me!", padx=50, pady=70, width=30,height=5, command=clickedme,fg="white", bg="green")
my_button.pack()
root.mainloop()