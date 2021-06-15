from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.geometry("500x200")
        self.attr1 = ""
        master.title("A simple GUI")

        self.label1 = Label(master, text="Enter a value in this input :", bg="#10D3D5").grid(row=0, column=4)
        self.entry1 = Entry(master).grid(row=1, column = 4)
        self.label2 = Label(master, text="This is a string with color", fg="#3300CC").grid(row=2, column=4)
        self.var = DoubleVar() 
        self.slider =  Scale(master, from_=0.00, to=1.0,orient=HORIZONTAL, length=400, variable = self.var,tickinterval=0.1, resolution=0.01, command="").grid(row = 3, column=4)
        self.greet_button = Button(master, text="Accept", command=self.accept).grid(row=15, column=1)
        self.close_button = Button(master, text="Fail", command=self.quit1).grid(row=15, column=7)
        

    def accept(self):
        self.attr1 = True
        self.master.quit()
    def quit1(self):
        self.attr1 = False
        self.master.quit()
def test():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
    li = []
    li.append(my_gui.attr1)
    li.append(my_gui.var.get())
    return(li)
